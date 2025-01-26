
# Python

Python je interpretovaný multiparadigmatický slabě typováný programovací jazyk.
Jeho hlavním moty jsou **Explicit is better than implicit**,
**Beautiful is better than ugly** a **Errors should never pass silently**.

## Základní zdroje

- Výborná kniha pro seznámení s Pythonem je [Ponořme se do Python(u)](http://knihy.nic.cz/)
- [30 Python Language Features and Tricks You May Not Know About](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html)
- Interaktivní [tutorial od sololearn](http://www.sololearn.com/Course/Python/)

## Modules

## Virtual enviroment

Jsou izolovaná prostředí pro Python. 

## pip

Pip je distribuční systém pro python. Má stadardní ovládání:

```bash
pip search wget
sudo pip install wget
sudo pip uninstall wget
```

Nainstalování libovolného (kompatibilního) repozitáře:

```bash
pip install git+http://github.com/kedrigern/pyexample
pip install <local/path>
```

I takovéto repozitáře jdou přes pip odinstalovat.

Pip umí fixovat verze a instalovat update:

```bash
pip install --upgrade <package>
```

## Weby

Nejpopulárnějším webovým frameworkem pro Python je Django.
Avšak já preferuji microframework [flask](flask.md).


