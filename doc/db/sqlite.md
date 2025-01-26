
SQLite
======

Je DB, která je uchována v jednom souboru (`*.db`). Díky typové afinitě je schopna pracovat s SQL v mnoha dialektech. Neznámé typy převádí na své nativní:

* NULL. The value is a NULL value.
* INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
* REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
* TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
* BLOB. The value is a blob of data, stored exactly as it was input.

Příkazy
-------

Ovládá se pomocí SQL. Příkazy mimo DB začínají `.` na začátku.

Vstup do shellu DB:
```
sqlite3 mydb.db [SQL]
```

Popřípadě můžeme příkaz rovnou vyvolat:
```
sqlite3 data.db -column -header "SELECT * FROM comment WHERE gid = 360001025;"
```

Csv:
```
.import <file>.csv <table>
```

```
.mode csv
.output <file>.csv
```

Pro hezký výpis je třeba:
```
.mode column
.header on
```

Další užitečné příkazy:

```
.help
.schema
.tables
.quit
```



Příklad
-------

Zadání 1: Mám velké CSV (`<file>.csv`) v kódování UTF-8:

```
$ sqlite3
.separator ","
.import <file>.csv <tablename>
select some_col from <tablename> limit 10;
[ výpis DAT ]
.backup <file>.db
```

Tím docílíme toho, že budeme mít daný soubor <file>.csv v databázi v tabulce <tablename>, sloupce se budou jmenovat dle prvního řádku. Bohužel všechny budou mít typ TEXT. Čili si opravíme názvy sloupců a typy (což se bude velmi hodit např. při exportu do jiné DB). Provedeme to postupem:

1. Vytvoříme novou tabulku
2. Převedeme do ní správně typované hodnoty

```sql
CREATE TABLE <tablename2>(...);
INSERT INTO <tablename2> SELECT CAST(some_col as INTEGER),b FROM <tablename>;
```

Pokud bychom chtěli původní tabulku nahradit (zachovat jméno), tak to musíme udělat o něco složitěji. Vytvořit dočasnou tabulku, smazat původní, vytvořit cílovou tabulku. Takovýto komplex operací je dobré dát do jedné transkce:

```sql
BEGIN;
CREATE TEMPORARY TABLE t1_backup(a INTEGER, b);
INSERT INTO t1_backup SELECT CAST(a as INTEGER),b FROM t1;
DROP TABLE t1;
CREATE TABLE t1(a INTEGER,b);
INSERT INTO t1 SELECT a,b FROM t1_backup;
DROP TABLE t1_backup;
COMMIT
```

# Odkazy

- [Integrace s Pythonem](../python/sqlite/sqlite.py)
