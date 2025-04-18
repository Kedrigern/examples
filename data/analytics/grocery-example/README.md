# Complex data example

Máme umělá data z obchodního řetězce. Ukážeme si práci s nimi za použití DuckDB či PostrgreSQL.

## Úvod

## Příprava dat

Pokud máme k dispozici, tak si přečteme dokumentaci či anotace dat. 

Průzkum dat samotných. Data máme ve formátu `csv`, což není záruka kvality a konzistence,
proto je vždy třeba nahlédnout, zda data odpovídají našim představám. Například i jednoduchá věc
jako primární klíč může být typu int, uuid, ale třeba i string (typicky kód zboží).

Pro nahlednutí se hodí příkazy `cat`, `head` resp. `bat`,  a `wc`. Mějme napaměti, že soubor může
obsahovat miliony řádků a grafické nástroje s tím mohou mít problém nebo budou zbytečně pomalé.

```bash
$ wc -l data/*csv  # Počet řádků v souboru
20 data/products.csv
26 data/purchases.csv
46 total
$ head data/*csv
[files content]
```

Hned vidíme kolik máme záznamů, zda máme hlavičku a obecný přehled o dokumentu. 
Zajímavou alternativou k příkazům `head` a zvláště pak `cat` je `bat`. Jedná se
o vylepšený `cat` v defaultu čísluje řádky, zvýrazňuje syntaxi prog. jazyků, stránkuje, 
zvýrazňuje csv, umí zvýraznit rozdíly dle git. Základní použití:

```bash
$ bat data/products.csv
[show file content with rainbow csv]
$ bat -r 1:25 data/products.csv     # Zobrazí řádky 1 až 25. r = range
$ bat -pp data/products.csv         # Prostý text bez stránkování. pp = plain, pagination
```

Další tip je použít příkaz `column`, avšak ten neumí ošetřit oddělovač v textech, čili 10 řádek
nezobrazí správně:

```bash
$ head data/products.csv | column -t -s ","
[table view of file]
```

## Struktura dat

Soubor `products.csv` obsahuje prodejní položky, struktura je přímočará. 

U souboru `purchases.csv` je situace jiná. Každý řadek je prodaná položka.
Řádky se slučují do jednotlivých nákupu. Každý nakup má společné zakazníka (`uuid`),
čas nákupu (`timestamp`), id nákupu (`purchase_id`) a celkovou cenu (`price`).
Tyto data tedy nejsou normalizovaná.

Platí tedy:

1. `purchase_id` má stejné: `uuid`, `timestamp`,`purchase_id`,`price` 
2. `price = sum(price_item_total)` pro dané `purchase_id`
3. `price_item_total = i_quantity * price_per_item` pro daný řádek (řadek 7 bug)
4. výjimkou jsou věci prodavané na váhu

Později si zkusíme dotazy, zda tyto invarianty platí.

## DuckDB a import dat

DuckDB je jednoduchá DB podobná SQLite. Data jsou uložena v jednom souboru.
Ale přesto je docela mocná a výkonná. Je plně integrovaná do programovacích jazyků,
to zajišťuje velkou přenositelnost a jednoduchý deployment. Avšak můžeme si ji 
stahnout i jako samostatnou aplikaci. Umí primární klíče, indexy cízí klíče.
Snaží se držet PSQL dialektu.

DuckDB můžeme mít jako samostanou aplikaci. Následně:

```bash
./duckdb                # in memory
./duckdb data/data.db   # data se ukládají do souboru data/data.db
```

Běžné použití SQL:
```sql
SELECT now() as now, TIMESTAMP '2020-06-01' as d2020, TIMESTAMP '1999-01-01' as d1999, now > d2020, d2020 BETWEEN d1999 AND now;
PRAGMA database_list;
PRAGMA show_tables;
CREATE TABLE user (
      uuid BIGINT PRIMARY KEY,
      name VARCHAR NOT NULL,
      email VARCHAR UNIQUE CHECK ((NOT contains(email, ' ')) AND contains(email, '@')),
      rating INT CHECK (rating >= 0));
ALTER TABLE user RENAME uuid TO id; 
CREATE INDEX u_idx ON user (rating);
CREATE TABLE inventory (
    id BIGINT PRIMARY KEY,
    item VARCHAR NOT NULL,
    user_id BIGINT REFERENCES user(id), -- FK
);
```

Nejzajímavější je import dat. Z CSV nejjednodušeji uděláme tabulku:

```sql
CREATE TABLE my_table AS 
      SELECT * FROM read_csv('data.csv');
```

Avšak takto přijdeme o možnost určit primární klíč. Můžeme nejdřív jen zjistit schéma:

```sql
SELECT * FROM sniff_csv('data.csv');
.mode line
SELECT Prompt FROM sniff_csv('data.csv');
.mode box
```

Nyní máme `read_csv` funkci se všemi parametry, snadno již nastavíme PK, UNIQUE či NOT NULL flagy u položky. Akorát to zatím nefunguje :(, tak lze použít AI:

```sql
CREATE TABLE product (
    id BIGINT PRIMARY KEY,   -- changed PK
    short_description VARCHAR,
    long_description VARCHAR,
    supplier_ico VARCHAR,
    status VARCHAR NOT NULL, -- changed not null
    bio BOOLEAN,             -- changed type
    vegiie BOOLEAN,          -- changed type
    tag1 BOOLEAN,            -- changed type
    tag2 BOOLEAN,            -- changed type
    tag3 BOOLEAN,            -- changed type
    tag4 BOOLEAN,            -- changed type
    timestamp_imported TIMESTAMP
);
CREATE TABLE purchase (
    id BIGINT PRIMARY KEY,   -- changed PK
    uuid UUID NOT NULL,      -- changed tye, not null
    article BIGINT,
    timestamp TIMESTAMP,
    store_site INT,
    i_quantity BIGINT,
    i_measurement BIGINT,
    price_per_item DECIMAL CHECK (price_per_item > 0),  -- type double does not exists in PGSQL
    price_item_total DECIMAL,        -- changed type
    price DECIMAL CHECK (price > 0), -- changed type
    purchase_id BIGINT,
    category VARCHAR,
    promotion BOOLEAN        -- changed type
);
-- Add indexes:
CREATE INDEX order_idx ON purchase (purchase_id);
CREATE INDEX article_idx ON purchase (article);
-- Copy data from csv:
COPY product FROM 'data/product.csv';
COPY purchase FROM 'data/purchase.csv';
```

Návod je kompatibilní i pro PostgreSQL. Příkaz copy je v ní též, ale oprávnění jsou složitější. Nicméně příkaz `\copy` vše zařídí z klienta:
```sql
-- GRANT pg_read_server_files TO <user>;
\copy product FROM './data/product.csv' WITH (format csv, delimiter ',', header);
```

Pro lepší práci si můžeme vytvořit view a díky tomu mít lepší pojmenování a vynechat sloupce, které v této části analýzy nechceme. Anebo, pokud to velikost dat dovolí, tak dokonce můžeme udělat pohled, kde jsou data propojena:

```sql 
CREATE OR REPLACE VIEW order AS
      SELECT o.id, o.uuid as customer_id, purchase_id, p.long_description as description,
      o.i_quantity as quantity, i_measurement as measurement, price_per_item,
      price_item_total, price as price_order_total,
      (bio or vegiie) AS healthy
      FROM purchase o LEFT JOIN product p ON o.article;
```

Tímto máme připravenou mocnou datovou základnu pro další práci.

SQL je robustní základ a soubory najednou máme datově rozumně v jednom souboru.
Ale ta pravá síla se objeví až když začneme DuckDB využívat přímo v pythonu:

```python
import duckdb as dd
import pandas as pd

con = dd.connect('data/data.db')

con.execute("CREATE ...") 

res = con.sql("SELECT * FROM order;")

res.show() # print to the terminal
data: tuple | None = res.fetchone()
data: list[any] = res.fetchall()
data: pd.DataFrame = res.df()
```

Čili jsme s daty schopni bez jakékoliv mezivstrvy pracovat v pythoních strukturách či v pandas dataframe.

## Pandas

## Dotazy

```sql
-- Objednávka 104:
SELECT * FROM order WHERE purchase_id = 104;

-- Ověření její ceny:
SELECT sum(price_item_total) FROM order WHERE purchase_id = 104;

-- ID všech nákupů zákazníka 'c1799f82-b43c-45c2-8255-8aa869b582f6':
SELECT DISTINCT(purchase_id) FROM order WHERE customer_id = 'c1799f82-b43c-45c2-8255-8aa869b582f6';

-- Kolik zákazník zaplatil celkem:
SELECT sum(price_item_total) FROM order WHERE customer_id = 'c1799f82-b43c-45c2-8255-8aa869b582f6';

-- Kolik zaplatil za jednotlivé nákupy:
SELECT distinct(purchase_id), price_order_total, customer_id FROM order WHERE purchase_id IN 
    (SELECT DISTINCT(purchase_id) FROM order WHERE customer_id = 'c1799f82-b43c-45c2-8255-8aa869b582f6');

-- Co zákazníci nakupovali nejčastěji (položka bez ohledu na množství)
SELECT description, count(*) AS amount FROM order GROUP BY description ORDER BY number desc;

-- Co zákazníci nakupovali nejčastěji kusů
SELECT description, sum(quantity) AS amount FROM order GROUP BY description ORDER BY number desc;

-- Co zákazník c17 nakupoval nejčastěji
SELECT description, sum(quantity) AS total_amount FROM order WHERE customer_id = 'c1799f82-b43c-45c2-8255-8aa869b582f6' GROUP BY description ORDER BY total_amount DESC;

-- Co zákazníci nakupovali nejčastěji per zákazník
SELECT customer_id, description, SUM(quantity) AS total_quantity FROM order GROUP BY customer_id, description ORDER BY customer_id, total_quantity DESC;
```

