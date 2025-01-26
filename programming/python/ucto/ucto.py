#!/usr/bin/env python3
"""
Parsování dokladů z pirátské wiki do csv

1. Dataplugin v Docuwiki ukladá data do sqlite2, tu si stáhneme:
scp <path>/data.sqlite ucto2.db
2. Nejdřívě je třeba převést sqlite2 do sqlite3:
sqlite ucto2.db .dump | sqlite3 ucto3.db   # konverze sqlite 2 do sqlite 3
3. Potom spustit tento skript

Parsování přímo z webu: https://github.com/pirati-byro/fo-vydaje2017 (zbytečně vytěžující a zdlouhavé)
"""

import csv
import sqlite3

year = '2017'
dbfile = 'ucto3.db'
csvfile = 'ucto' + year + '.csv'
vydaje = []

def parsePolozka(pol):
    """
    input format:
        fo:hospodareni2017:rozpocty:strana:212800001
    return
        (stredisko, polozka_num)
    """
    try:
        ns = pol.split(':')
        pair = (ns[-2], ns[-1])
        return pair
    except:
        return ('stana', '')

def processVydaj(records, results):
    """
    Procces multiple records with key, vals into one object, for example:
    sqlite> select * from data where pid = 482;
    eid         pid         key         value
    ----------  ----------  ----------  ----------
    14848162    482         značka     FO 20/2014
    14848163    482         číslo     20
    14848164    482         složka     regiony:pl
    14848165    482         hospodář  lide:lukas
    14848166    482         položka    fo:hospoda
    14848167    482         záměr     Proplacen�
    14848168    482         účel      volné pen
    14848169    482         příjemce  Lukáš V�
    14848170    482         účet      1204210039
    14848171    482         vs          123456789
    14848172    482         ks
    14848173    482         částka    -1167.50
    14848174    482         doklad      není pot�
    14848175    482         podáno     2014-02-16
    14848176    482         proplaceno  2014-02-17
    14848177    482         souhlas     https://ww
    """
    vydaj = {}
    for item in records:
        key = item[2]
        val = item[3]
        if key == 'položka':
            if val == '':
                return  # nejedná se o vydaj
            vydaj['středisko'], vydaj['položka'] = parsePolozka(val)
            continue
        vydaj[item[2]] = item[3]
    results.append(vydaj)

with sqlite3.connect(dbfile) as conn:
    c = conn.cursor()
    namespace = 'fo:vydaje:fo_%_' + year
    args = (namespace,)
    pids = c.execute("select pid from pages where page like ?;", args).fetchall()
    for row in pids:
        pid = row[0]
        records = c.execute("select * from data where pid = '%d'" % pid).fetchall()
        processVydaj(records, vydaje)

with open(csvfile, 'w') as csvw:
    fieldnames = ['značka', 'středisko', 'položka', 'částka', 'podáno', 'proplaceno', 'redmine', 'popis'] # jakub
    fieldnames = ['značka', 'středisko', 'položka', 'částka', 'podáno', 'proplaceno', 'souhlas', 'usnesení', 'název', 'vs', 'příjemce', 'záměr', 'doklad', 'ks', 'rok', 'druh', 'ss', 'účet', 'číslo', 'účtováno', 'hospodář', 'rest', 'zdroj', 'složka', 'účel'] # full
    writer = csv.DictWriter(csvw, fieldnames=fieldnames)
    writer.writeheader()
    for vydaj in vydaje:
        try:
            writer.writerow(vydaj)
        except ValueError as e:
            print(vydaj)
            print(e)
