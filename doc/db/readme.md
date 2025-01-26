# Databáze

- SQL
  - [PostgreSQL](postgres.md)
  - [MySQL](mysql.md)
  - [SQLite](sqlite.md)
- [ldap](ldap/readme.md)
- [neo4j](neo4j/readme.md)

# SQL

Je univerzální dotazovací jazyk pro relační databáze. Naneštěstí každá DB používá mírně jiný dialekt.

## Basic interact

<table>
  <thead>
    <tr>
      <th rowspan=2>What</th>
      <th colspan=3>Command</th>
      <th rowspan=2>Note</th>
    </tr>
    <tr>
      <th>psql</th>
      <th>mysql</th>
      <th>SQLite</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>Port</td>
    <td>5432</td>
    <td>3306</td>
    <td />
    <td />
  </tr>
    <tr>
      <td>Connect server</td>
      <td>psql</td>
      <td>mysql -u &lt;user&gt; -p</td>
      <td>sqlite3 mydb.db</td>
      <td />
    </tr>
    <tr>
      <td>Shell</td>
      <td>\! &lt;cmd&gt;</td>
      <td>\! &lt;cmd&gt;</td>
      <td />
      <td />
    </tr>
    <tr>
      <td>Load file</td>
      <td>\i &lt;filename&gt;.sql</td>
      <td>\\. &lt;filename&gt;.sql</td>
      <td>.read &lt;filename&gt;.sql</td>
      <td />
    </tr>
    <tr>
      <td>List DB</td>
      <td>\l</td>
      <td>show databases;</td>
      <td />
      <td />
    </tr>
    <tr>
      <td>Connect DB</td>
      <td>\c &lt;db&gt;</td>
      <td>use &lt;db&gt;;</td>
      <td />
      <td>\c = connect</td>
    </tr>
    <tr>
      <td>Help</td>
      <td>\h</td>
      <td>help</td>
      <td>.help</td>
      <td></td>
    </tr>
    <tr>
      <td>List table</td>
      <td>\dt</td>
      <td>show tables;</td>
      <td>.tables</td>
      <td/>
    </tr>
    <tr>
      <td>Describe table</td>
      <td>\d &lt;table&gt;</td>
      <td>DESCRIBE &lt;table&gt;;</td>
      <td>.schema &lt;table&gt;</td>
      <td/>
    </tr>
    <tr>
      <td>Describe index</td>
      <td>\di</td>
      <td>SHOW INDEX FROM &lt;table&gt;;</td>
      <td/>
      <td/>
    </tr>
  </tbody>
</table>

## SQL

Budeme pracovat s ukázkovou tabulkou:

|id | name | salary | born       | department |
|---|------|--------|------------|------------|
| 1 | Ala  | 20 800 | 1990-09-20 | A          |
| 2 | Alan | 21 600 | 1989-10-20 | A          |
| 3 | Anna | 22 500 | 1988-11-15 | A          |
| 4 | Lala | 23 500 | 1987-12-01 | L          |
| 5 | Leo  | 22 100 | 1986-05-13 | L          |

U SQLite není id autoincrement, ale vnitřně vždy existuje sloupec `rowid`, vyvoláme ho: `SELECT rowid, * FROM people;`

### Create DB and insert

```sql
CREATE TABLE people (
 id serial primary key,
 name varchar(50),
 salary real,
 born date,
 department varchar(50)
);

INSERT INTO people (name, salary, born, department) VALUES
 ('Ala',  20800, '1990-09-20', 'A'),
 ('Alan', 21600, '1989-10-20', 'A'),
 ('Anna', 22500, '1988-11-15', 'A'),
 ('Lala', 23500, '1987-12-01', 'L'),
 ('Leo',  22100, '1986-05-13', 'L');
```

U MySQL je třeba nahradit typ `serial` za `int` (autoincrement je doplněn automaticky).

### Import a Export csv

<table>
  <thead>
    <tr>
      <th>cmd</th><th>psql</th><th>mysql</th><th>sqlite</th>
    </tr>
  </thead>
  <tr>
    <td>import</td>
    <td><code>\COPY people FROM 'data.csv' WITH CSV HEADER;</code></td>
    <td><code>
    LOAD DATA INFILE "data.csv" INTO TABLE people IGNORE 1 LINES;</code></td>
    <td><code>.separator ","
    .import data.csv people</code></td>
  </tr>
  <tr>
    <td>export</td>
    <td><code>\COPY people TO 'data2.csv' WITH CSV HEADER;</code></td>
    <td><code>mysql -e 'select * from people' -B > data2.tsv</code></td>
    <td><code>.mode csv
    .output data2.csv</code></td>
  </tr>
  <tr>
    <td>note</td>
    <td>
    <code>COPY</code> je interní, běží na DB stroji, zatímco <code>\COPY</code> běží pod userem s kterého jsme připojeni (který zadal <code>psql</code>).
    </td>
    <td>
    U MySQL je třeba nastavit příslušná práva uživateli: <code>grant file on *.* to keddie identified by 'keddie';</code>
    </td>
    <td />
  </tr>
</table>

### Select

```sql
SELECT * FROM people ORDER BY salary DESC;

SELECT * FROM people WHERE name LIKE 'Ala%';
SELECT * FROM people WHERE name LIKE 'Ala_';
SELECT * FROM people WHERE name LIKE '%la%';

SELECT * FROM people WHERE born < '1987-01-01';
SELECT * FROM people WHERE born BETWEEN '1987-01-01' AND '1989-01-01';
```

### Update

```sql
UPDATE people SET salary=22900 WHERE id=5;
UPDATE people SET id=id+100;
```

### Group by

```sql
SELECT department, count(name) AS 'num of people', sum(salary) as 'total salary'
FROM people GROUP BY department;

SELECT born<'1988-1-1', count(name), sum(salary) FROM people GROUP BY born<'1988-1-1';
```

### Join

![](sql-joins.png)


Přidáme si tabulku `department`:

| id | name | nanager_id |
|----|------|------------|
|  1 | A    | 3          |
|  2 | L    | 4          |

```sql
CREATE TABLE department (
	id int,
	name varchar(50),
	manager_id int
);
INSERT INTO department (name, manager_id) VALUES
 ('A', 3),
 ('L', 4);
```

```sql
SELECT people.name, salary, born, department,
 (SELECT people.name from people WHERE people.rowid=department.manager_id) AS Manager
FROM people LEFT JOIN department ON people.department = department.name;
```
### Create view

```sql
CREATE VIEW summary AS
SELECT people.name, salary, born, department,
 (SELECT people.name from people WHERE people.rowid=department.manager_id) AS Manager
FROM people LEFT JOIN department ON people.department = department.name;
```

### Komplexní dotazy

Pokud máme data uložená jako [EAV](https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model):

| id | key | val |
|----|-----|-----|
|  1 | a   | a1  |
|  1 | b   | b1  |
|  2 | a   | a2  |
|  2 | b   | b2  |
|  3 | a   | a3  |
|  3 | b   | b3  |

```sql
create table t1 ( id, key, val );
insert into t1 values
  (1, 'a', 'a1'), (1, 'b', 'b1'), (2, 'a', 'a2'), (2, 'b', 'b3'), (3, 'a', 'a3'), (3, 'b', 'b3');
```

A chceme dostat klasickou tabulku:

| id | a | b |
|----|---|---|
|  1 | a1| b1|
|  2 | a2| b2|
|  3 | a3| b3|

```sql
select ent.id, a.val a, b.val b from
  (select distinct id from t1) ent
  left join t1 a on a.id = ent.id and a.key = 'a'
  left join t1 b on b.id = ent.id and b.key = 'b';
```
----

| id | num | date       |
|----|-----|------------|
| 1  |  50 | 2017-01-10 |
| 1  |   0 | 2017-02-10 |
| 2  |  60 | 2017-01-10 |
| 2  |   0 | 2017-02-10 |

| id | comment           |
|----|-------------------|
|  1 | first line for 1  |
|  1 | second line for 1 |
|  2 | comment text for 2|


```sql
create table record ( id, num, date );
create table comment ( id, comment );
insert into record values (1, 50, '2017-01-10'), (1, 0, '2017-02-10'), (2, 60, '2017-01-10'), (2, 0, '2017-02-10');
insert into comment values (1, 'first line for 1'), (1, 'second line for 1'), (2, 'comment text for 2');

-- Potřebuji spojit následující dva pohledy:

select id, group_concat(comment) as comment from comment group by id;
select * from record where num > 0;

-- Čehož docílím:
select r.id, r.num, r.date, c.comment
  from record r left join
    (select id, group_concat(comment, ',') as comment from comment group by id) c
    on c.id = r.id
  where num > 0;
```
A výsledek:

| id  | num  |   date     |   comment                          |
|-----|------|------------|------------------------------------|
| 1   |   50 | 2017-01-10 | first line for 1,second line for 1 |
| 2   |   60 | 2017-01-10 | comment text for 2                 |
