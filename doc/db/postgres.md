# PostgreSQL

## Instalace

Samotná instalace Fedora 23:
```
sudo dnf install postgresql-server postgresql-contrib
sudo systemctl enable postgresql
sudo postgresql-setup --initdb --unit postgresql
sudo systemctl status postgresql
```

Konfigurace:
```
su root
su - postgres
```

Konfigy:
```
/var/lib/pgsql/data/postgresql.conf	# obecný konfig
/var/lib/pgsql/data/pg_hba.conf 	# nastavení přístupů
```

### Autentifikace

- trust: kdokoliv z daného os
- password: nehashované heslo (ošetřuje se pomocí SSL)
- md5: hashované heslo
- GSSAPI: SSO, kerberos
- SSPI: SSO windows,
- ident: ident server, dobrý pro TCP/IP
- peer: pouze loakální
- ldap
- radius
- certificate
- pam

## Terminal

### pqsl


| PG         | Description       |
|------------|-------------------|
| \q  	     | quit              |
| \l  	     | list of databases |
| \dt        | list of tables    |
| \c <dbname>| connect to dbname |
| \h <cmd>   | help for comand   |

### pgsql

`psql -U <username> -h <hostname> -d <dbname>` nás připojí k serveru, můžeme zde normálmě zadávat SQL příkazy. Vypneme ho příkazem `\q`.

### pg_dump


`pg_dump -U <username> -h <hostname> <dbname>` dumpne DB na stdout. Užitečné parametry:

`-s` dumpne pouze schéma db

`--data-only` dumpne pouze data

`-f <outputfile>` výstupní soubor

`-t <tablename>` dumpne konkrétní tabulku

`-T <tablename` vynechá zadané tabulky

`-E <encoding>`

`--compress=<0..9>` nastavení úrovně komprese (0 žádná)

`--help` nápověda

`-O` přeskočí vlastnictví

### pg_restore

`pg_dump -U <username> -h <hostname> -d <dbname> <filename>` obnoví soubor filename, který jsme předtím získali skrze `pg_dump`.

`--help` nápověda

### .pgpass

Je soubor s přístupovými údaji. Musí mít správná oprávnění (přístup jen vlastník) a má následující formát:

```
hostname:port:database:username:password
```

lze v něm psát komentáře skrze `#`.


### Příklad zálohy

```bash
pg_dump -h <host> -U <user> -s <dbname> > schema.sql # zaloha schematu db
pg_dump -h <host> -U <user> --data-only <dbname> > data.sql # zaloha dat z db
```

jelikož si spojení uložíme do .pgpass, tak nemusíme ani zadávat heslo.


## Práva
Postgres velmi využivá uživatleských práv a rolí.


`GRANT UPDATE ON <table> TO <user>;` garantuje práva pro dané tabulky

`GRANT UPDATE ON ALL TO <user>;` garantuje všechna práva

`CREATE ROLE <name>` vytvoří roli

`DROP ROLE <name>;`

## Datové typy

* [Souhrn](http://www.postgresql.org/docs/9.2/static/datatype.html)

Zajimavé je, že Postgres umí pole, geometrii, síťové adresy, xml, json, ...

`serial` sekvence, čili automaticky se inkrementující typ pro indexy

`numeric` číslo s libovolnou přesností. `NUMERIC(precision, scale)` precision je celkový počet číslic a scale jsou ty za desetinou čárkou.

`timestamp` a `timestamptz` časová známka, bez a s timezone.

`uuid` dle [RFC 4122](http://www.ietf.org/rfc/rfc4122.txt), čili sequence of lower-case hexadecimal digits, for a total of 32 digits representing the 128 bits

### Důležité definice

```sql
CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
```

## Postrgres v Nette

### bootstrap.php

```php
// DIBI
$configurator->onCompile[] = function($configurator, \Nette\Config\Compiler $compiler) {
    $compiler->addExtension('dibi', new DibiNetteExtension() );
};
```

dibi.neon:

```
dibi:
    driver: postgre
    host: localhost
    username:
    password:
    database:
    lazy: true
```
config.neon:

```
	includes:
		- dibi.neon
```
composer.json:

```json
 "require": {
    "php": ">= 5.3.0",    
    "nette/nette": ">= 2.0.7",
    "dg/dibi": "2.0.*"
  }
```

Nezapomenout nahradit: `Nette\Database\Connection` na `DibiConnection`.

## Grafičtí správci

### tora
`sudo apt-get instal tora libqt4-sql-psql`

## Integrované funkce

Lze použít spoustu jazyků, já zvolil Python.

### Inicializace

U DB je třeba nejdříve jazyk načíst:

```bash
sudo apt-get install postgresql-plpython-9.2
```

Zda máme Python správně nainstalovaný v DB zjistíme:

```sql
SELECT *
FROM pg_pltemplate
WHERE tmplname LIKE 'plpython%'
```

Následně v DB spustíme:

```sql
CREATE LANGUAGE plpython3u
```

Odteď máme jazyk inicializovaný.

### Práce s funkcemi

#### Seznam všech uložených funkcí:

```sql
SELECT  proname
FROM    pg_catalog.pg_namespace n
JOIN    pg_catalog.pg_proc p
ON      pronamespace = n.oid
WHERE   nspname = 'public'
```

#### Nová funkce

```sql
CREATE OR REPLACE FUNCTION pymax (a integer, b integer)
  RETURNS integer
AS $$
  if a > b:
    return a
  return b
$$ LANGUAGE plpython3u;

```

Pracoval jsem i s pokročilejšími skripty, které importovali knihovny, obsahovali funkce, třídy etc. Dokonce jsem i zpětně pracoval z Pythonu s DB.

Pro editaci a testování doporučuji PGadmin, který umí funkce docela dobře spravovat, zvýrazňuje syntaxi etc.

* [prezentace k tématu](http://www.postgresqlconference.org/sites/default/files/PLPython.pdf)

### Fulltext search via Tsearch
####  Instalace
```bash
cd /usr/share/postgresql/9.2/tsearch_data/ # path for v9.2 in Ubuntu 12.10
wget -qO- http://www.pgsql.cz/data/czech.tar.gz | tar xz
mv fulltext_dicts/* . && rmdir fulltext_dicts
```

Následně pod superuživatelem DB spustíme:
```sql
CREATE TEXT SEARCH DICTIONARY cspell
   (template=ispell, dictfile = czech, afffile=czech, stopwords=czech);
CREATE TEXT SEARCH CONFIGURATION cs (copy=english);
ALTER TEXT SEARCH CONFIGURATION cs
   ALTER MAPPING FOR word, asciiword WITH cspell, simple;
```

#### Tvorba indexu
Index nad sloupcem připravíme:

```sql
CREATE INDEX <tabulka>_<sloupec>_ftx ON <tabulka>
   USING gin(to_tsvector('cs', <sloupec>))
```

Můžeme udělat i index nad více sloupci:

```sql
CREATE INDEX <tabulka>_<sloupec>_ftx ON <tabulka>
   USING gin(to_tsvector('cs', <sloupec1> || ' ' || <sloupec2>))
```

Abychom sloupcům zachovali význam (nadpis důležitější než popis), tak jim můžeme nastavit váhu:


#### Hledání

Použití pro hledání:
```sql
SELECT * FROM <tabulka>
  WHERE
to_tsvector('cs',<sloupec>) @@ to_tsquery('<term1> & <term2>')
```

Hledání je case insensitive. Používají se logické operátory `&` (and), `|` (or), `!` (not).

Popřípadě se občas hodí nahradit `cs` za `simple`, pokud nechceme lexikální vyhodnocování (to je občas poněkud neočekávané).

#### Odkazy
* Souhrn fulltextových technologii a provonání rychlosti:
[full-text-search-in-postgresql](http://www.slideshare.net/billkarwin/full-text-search-in-postgresql)
* [Dokumentace Tsearch](http://www.postgresql.org/docs/9.0/interactive/textsearch-controls.html)
* [Triggers for Automatic Updates](http://www.postgresql.org/docs/8.3/static/textsearch-features.html#TEXTSEARCH-UPDATE-TRIGGERS) (kompletní ukázka)


## Odkazy

* [Fedora doc](https://fedoraproject.org/wiki/PostgreSQL)
* [Po instalaci](http://stackoverflow.com/questions/1471571/how-to-configure-postgresql-for-the-first-time)
* [Článek z roku 2003](http://www.abclinuxu.cz/clanky/navody/prakticky-navod-k-pgsql)
* [Správa uživatelů](http://www.davidpashley.com/articles/postgresql-user-administration/)
