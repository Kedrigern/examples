
Bash scripts
============

* [md2pdf](md2pdf.sh): Convertor for nautilus scripts
* [adoc2md](adoc2md.sh):
* [findPdf](findPdf.sh):  Search pattern in all pdf files in actual directory. Use pdftotext for convert - it`s main limit of this script.
* [html2epub](html2epub.sh): html2epub via pandoc with GUI (Zenity). Some mechanism for cleaning html code.


Tutorial
--------

### Co je to Bash?

V Linuxu je všude. Typicky, když otevřeme terminál, tak používáme bash.
Je to základní sada příkazů jakými jsou: `ls`, `mv`, `cp`, ... a syntaxe okolo nich.
Popř. bychom mohli říct scriptovací jazyk. Uživatelé Windows by možná řekli jazyk pro dávkové zpracování.

Celé prostředí terminálu je totiž programovací jazyk.
V terminálu ho používáme typicky po jednom příkazu (příkaz > enter),
ale to neznamená, že nejde používat i trochu jiným způsobem.

Pro základní práci je dobré naučit se základní příkazy.
Až pak se nám bude hodit syntax jako jsou smyčky, vstupy a výstupy a další pokročilejší praktiky.

Unix a z jeho filosofie vycházející bash pracuje s textem a soubory.
Jakákoliv entita v OS je soubor (např. existuje soubor reprezentující flashdisk) a v souboru je text.
Tato abstrakce umožňuje snadné zřetezení příkazů a práci s textem.
Samozřejmě, že pokud je soubor binární, tak nám daný text nic říkat nebude - termínál nám ho dokonce ani nezobrazí.

Bash je akronym Born again shell. Shell se nazývá tato rodina jazyků, popř. jazyk terminálu. Shell ve smyslu, že
obaluje systém a dovoluje nám s ním snadno pracovat. Je celá řada shellů: `sh`, `tsh`, `zsh`, `dash`, `bash`.
Bash je nejrozšířenější a jeden z nejinteraktivnějších. Ale není jediný používaný.
Např. dash je jednodušší (méně nachylný k chybám, menší binárka) a právě proto se používá pro
systémové scripty v Debianu.
Na druhou stranu je zbytečné jednodušší shelly používat pro skript, kterým si chceme upravit pár fotek z dovolené.

### Základní příkazy

| Příkaz | Význam                     | Příkaz |                |
|--------|----------------------------|--------|----------------|
| ls     | vylistování složky         | man    | manual         |
| mv     | move: přesun souboru       | sudo   | super user do  |
| cp     | copy: zkopírování souboru  | echo   | vypíše řetězec |
| rm     | remove: smazání souboru    | true   | vrátí true	|
| cd     | change dir: změna adresáře | false  | vratí false    |
| tr     | translate: nahrazení znaků | shift n| posun parametru o n|
| wc     | word count: počet slov     | du     | využití místa  |
| ln     | link:vytváří odkazy        | fg     | |
| su     | přepnutí uživatele         | bg     | |
| ps     | procesy v daném terminálu  | pwd    | print working dir |

A do jisté míry jakýkoliv další příkaz, který máme v systému.
Spustit z bashe můžeme i ty s grafickým rozhraním.
A velmi často je můžeme spustit bez grafického rozhraní - a využít je k dávkovému zpracování.

#### man

Příkazy mají manuálové stránky, které nás seznámí se základní funcionalitou a přepínačemi.
Proto si nemusíme detaily pamatovat, ale stačí zadat např. `man ls`.

#### sed, vim

Vim je textový editor v terminálu. Sed se ovládá stejně a jedná se o proudový editor textu.

```
sed [-n] 'script' [inputfile]
```

#### awk

### Hlavička

Na začátku skriptu píšeme: `#!/usr/bin/env bash`, což označuje interpret.
Bash nevoláme přímo, protože se v různých distribucích nachází na různých místech
(např. v Ubuntu nesprávně v: `/bin/bash`, zatímco ve Fedoře: `/usr/bin/bash`).

Dále je dobré uvést základní dokumentační komentáře:

```
Author: Joe Doe, mail@example.org
Licence: GPL
Dependency: gcc
Description: Short description
Todo: All funcionality
```

### Proměnné

```bash
HELLO=Hello
function hello {
	local HELLO=World
}
```

Proměnná se vyvolá s `$<nazev>`, pokud by hrozila záměna s jinou[^1], tak se lze použít `${<nazev>}`.

```bash
filecount=$( ls /etc | wc -l )
filename=${1%.txt}.md		# odebere z proměnné sufix ".txt" a přidá ".md" (nejkratší)
filename=${1%%.txt}.md		# odebere z proměnné sufix ".txt" a přidá ".md" (nejdelší)
filename=${1#hello}		# odebere z proměnné text "hello" (nejkratší)
filename=${1##hello}		# odebere z proměnné text "hello" (nejdelší)
```

#### Předdefinované

|    | popis                                       |
|----|---------------------------------------------|
| $* | Všechny poziční parametry.                  |
| $@ | Všechny poziční parametry.                  |
| $# | Počet parametrů                             |
| $? | Návratová hodnota posledního volání.        |
| $$ | ID procesu daného shellu                    |
| $! | ID procesu spuštěného v pozadí (posledního) |
| $0 | Jméno shellu / skriptu                      |
| $n | *n* je číslo 1-9, daný poziční parametr     |
| $_ | Z počátku skriptu je v ní plná cesta ke skriptu. Později v ní je poslední argument posledního příkazu. |
| $USER    | Uživatel pod kterým je shell spuštěn  |
| $HOSTNAME| Hostname systému                      |
| $SECONDS | Vteřin od spuštění skriptu            |
| $RANDOM  | Náhodné číslo                         |
| $LINENO  | Současná řádka skriptu                |

#### Argumenty

Argumenty (parametry) skriptu jsou již zmíněné `$*`. Zpracovávají se pomocí příkazu `shift`. 

Spustíme: `./run.sh --prvni a --druhy b`

Zpracujeme je:

```bash
if [ $# -gt 0 ]; then
	while [ $# -gt 0 ]; do
		case "$1" in
		"-p" | "--prvni")
			prvni="$2";
			shift 2;
		;;
		"-d" | "--druhy")
			druhy="$2";
			shift 2;
		;;
		*)
			echo "Unknow parametr";
			exit 1;
		;;
		esac;
	done;
else
	# Without parameters?
	:
fi;
```

#### Předání globálních parametrů

Scriptu můžeme předat globální parametr takto (předáváme proměnnou `LC_ALL`):

```
$ date
Po led  4 19:16:41 CET 2016
$ LC_ALL=cs_CZ.utf8 date
Po led  4 19:16:37 CET 2016
$ LC_ALL=de_DE.utf8 date
Mo 4. Jan 19:16:29 CET 2016
$ LC_ALL=en_US.utf8 date
Mon Jan  4 19:17:27 CET 2016
```


### Wildecards


|     | příklad| výsledek       | popis                                      |
|-----|--------|----------------|--------------------------------------------|
| *   | a*     | a, aa, a1, ... | jakýkoliv počet jakýhkoliv znaků (výjma .) |
| ?   | a?     | aa, ab, ...    | jeden libovolný znak                       |
| []  | a[b-e] | ab, ac, ad, ae | interval znaků                             |
| [!] | a[!c]  | nebude: ac     | negace předchozí možnosti                  |
| {}  | a{a,b} | aa, ab         | nebo                                       |


### Řízení běhu

```bash
if cmd1; then
  cmd2;
else
  cmd3;
fi;
```

```bash
case "$x" in
	start)
		cmd1;
	;;
	stop)
		cmd2;
	;;
	help*)
		cmd3;
	;;
	*)
		cmd4;
	;;
esac;
```

```bash
for i in *.txt; do
 cmd $i;
done;
```

### Funkce

I v bashy existují funkce. Jsou velmi omezené, dokonce ani neumějí vrátit hodnotu.
Nicméně samozřejmě pomohou:

- logickému dělení delšího kódu
- dokumentaci
- testování

Syntaxe:

```bash
function putTextIntoFiles() {
	text="$1"
	shift 1;
	for f in $@; do
		echo "$text" >> f
	done;
}
```

Funkce má proměnné `$1, ...`, což jsou její argumenty. A samozřejmě též může přistupovat ke globálním proměnným.

### Pajpy

Pipe je propojení výstupu jednoho programu se vstupem dalšího, např:
`echo "Lorem ipsum" | grep "Lorem" | wc -c`

Pokud bychom chtěli návratové hodnoty jednotlivých programů, tak je k tomu určena proměnná `PIPESTATUS`.
Pipes však vyvolávají subshelly, čili je dostupná pouze přímo v subshellu, kde jsou pipes:

`echo "Lorem ipsum" | grep "Lorem" | wc -c; echo ${PIPESTATUS[2]}`

Jedná se o bash array.

### Vstupy a výstupy

Bash má standardní vstup (`stdin`), standardní výstup (`stdout`) a standardní chybový výstup (`stderr`).
Výstupy a vstupy jsou operace nad soubory (jako vše v unixu). Proto můžeme vstupy jednoduše přesměrovávat:

```bash
echo "Normal info"			# vypíše na stdin - obvykle na příslušný terminál
echo "Normal info" > text.txt		# vypíše na stdin, což je soubor text.txt
echo "Normal info" >> text.txt		# vypíše na stdin, což je soubor text.txt, text připojí - nepřepíše
echo "Normal info" >> text.txt 2>&1	# vypíše na stdin, což je soubor text.txt, text připojí - nepřepíše, připojili jsme i chybový výstu
>&2 echo "error"			# echo píše na stderr
grep lorem < file.txt 2> /dev/null	# grep má stdin file.txt a chyby vypisuje do /dev/null
grep lorem < file.txt &> both.txt	# oba 2 výstupy do jednoho souboru
```

Ještě se hodí umět zapsat víceřádkový vstup:

```bash
cat > file.txt << EOF
Více řádkový soubor.
Přehledně zapsaný ve skriptu.
EOF
```

Tipy
----

### Odstanění zalomení

Máme soubor:

```
Lorem ipsum
Lorem ispum

Lorem ipsum
Lorem ipsum
```

To jest mezi odstavci je prázdný řádek.
A v rámci odstavce jsou zalomení.

Občas se hodí daná zalomení odstranit:

```
cat file | echo -n `sed 's/^$/STARTPARA/'` | sed 's/STARTPARA/\n/g'
```

### Rozdělení skriptu do více souborů

`base.sh` ukazuje jak můžeme načíst část skriptu (např. proměnné, funkce) z jiného skriptu. Což velmi pomůže čistotě kódu a např. i testování.


### Úkoly k procvičení

1. Zjistěte v jaké jste složce.
2. Vytvořte složku `tmp` a v 2 soubory. Jeden prázdný, druhý s obsahem `Hello world!`. Pojmenujte je: `1-empty.md` a `2-hello.md`
3. Změňte working directory na `tmp`
4. Vypiště obsah složky
5. Vypište soubory končící příponou `.md`
6. Vypiště soubory začínajcí číslicí `1`


# Další zdroje

- [writing-robust-shell-scripts][]
- [bash-promts][]

[writing-robust-shell-scripts]: http://www.davidpashley.com/articles/writing-robust-shell-scripts/
[bash-promts]: http://www.davidpashley.com/articles/bash-prompts/
