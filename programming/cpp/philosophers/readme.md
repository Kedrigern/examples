
# Problém obědvajících filosofů #


Tento program je jednoduchou praktickou simulací
[problému obědvajících filosofů](http://en.wikipedia.org/wiki/Dining_philosophers_problem)
 implementovanou v C++ (C++11).

### Základní použití ###
Parametr `-h` nebo `--help` zobrazí nápovědu.

Další parametry:

+----------+---------------+----------+---------+----------------------------+
| Zkrácený | Dlouhý        | Argument | Default |Popis                       |
+==========+===============+==========+======================================+
| -r       | --resources   | číslo    | 5       | Počet zdrojů (příborů).    |
+----------+---------------+----------+---------+----------------------------+
| -n       | --philosophers| číslo    | 5       | Počet večeřících filosofů. |
+----------+---------------+----------+---------+----------------------------+
| -s       | --starving    | číslo    | 3       | Počet kol po které může    |
|          |               |          |         | filosof hladovět.          |
+----------+---------------+----------+---------+----------------------------+
| -d       | --delay       |          |         | První filosof počká 1 kolo,|
|          |               |          |         | čímž může zamezit          |
|          |               |          |         | deadlocku.                 |
+----------+---------------+----------+---------+----------------------------+
| -p       | --polite      |          |         | Filosof vrátí vidličku     |
|          |               |          |         | (zdroj), když dojí nebo    |
|          |               |          |         | umře.                      |
+----------+---------------+----------+---------+----------------------------+
| -h       | --help        |          |         | Zobrazí nápovědu a skončí. |
+----------+---------------+----------+---------+----------------------------+

### Dokumentace ###
Dokumentace je napsána v markdownu.
Ten lze lehce převést do množství dalších formátů pomocí [pandoc]().

Převedení do pdf:

```
make doc-pdf
```

Převdení do html:

```
make doc-html
```

### Příklady použití ###

#### Deadlock ####
K deadlocku dojde pokud zavoláme program bez parametrů.
Bude použit stadartní počet filosofů (5) i zdrojů (5).
Filosofové nebudou vracet zdroje (jakmile jednou získají zdroj, tak ho nevratí).

Každý filosof vezme jeden zdroj, čili se v prvním kole vypotřebují všechny zdroje.
Jelikož zdroje nejsou vraceny, tak filosofové budou hladovět 3 kola (defaultní parametr).

Ověřit, že se opravdu jedná o deadlock můžeme snadno parametrem `--starving <num>` (`-s`), který
udává počet kol po které může filosof hladovět.
Pokud tento parametr zvětšíme, tak zjistíme, že filosofům to nepomůže - pouze prodlouží jejich hladovění.

#### Jeden přežije ####
Použijeme parametr `--delay` (`-d`), který pozdrží prvního filosofa.
Tím pádem jeden z dalších filosofů stihne získat 2 zdroje a tedy se úspěšně najíst.
Nicméně ostatní jsou stále v deadlocku, jelikož tento filosof po konzumaci zdroje nevrátí.

#### Většina přežije ####
Viděli jsme, že problémem je, že zdroje nejsou vraceny. To zařídí parametr `--polite` (`-p`).
Nicméně pokud program zavoláme jen s tímto parametrem, tak velmi pravděpodobně všichni filosofové
pomřou. Může se stát, že nějaký přežije, jelikož stihne vzít zdroje po vyhladovělém kolegovi.

Pokud chceme, aby opravdu většina přežila musíme dodat parametr `--delay` tím pádem jeden z filosofů jistě
přežije. Pokud přidáme počet kol (`--starving <num>`), tak jich bude přežívat více.
Při `--starving 5` již přežijí všichni.

### Zdroje ###
 * [Problému obědvajících filosofů](http://en.wikipedia.org/wiki/Dining_philosophers_problem)
 * [Deadlock](http://en.wikipedia.org/wiki/Deadlock)

### Licence ###
GPL version 3.

### Autor
Ondřej Profant, ondrej.profant <> gmail.com, https://github.com/Kedrigern
