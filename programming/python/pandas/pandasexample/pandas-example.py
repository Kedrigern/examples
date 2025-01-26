#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jednoduchá ukázka práce s knihovnou Pandas.
Ta slouží k úpravám tabulkových dat.
"""

import sqlite3
import math
import pandas as pd

datafile1 = "datafile.csv"
use_cols = ['a', 'b', 'c']  # use only these 3 cols, col d will be removed
to_del = ['d']              # remove column d

def load_csv():
    """1. Můžeme načíst csv a rovnou v něm profiltrovat řádky či sloupce."""

    # Use only some cols
    t1 = pd.read_csv(datafile1, sep=',', usecols=use_cols)

    # Drop some cols
    t2 = pd.read_csv(datafile1, sep=",")
    t2.drop(to_del, axis=1, inplace=True)

    print(load_csv.__doc__)
    print(t1.head(1))
    print(t2.head(1))

def load_sql():
    """2. Načítání z SQL"""

    # Fill DB with the data
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE table1 (
        id int,
        name varchar
    ) ''')
    values = (1, 'a')
    c.execute('INSERT INTO table1 VALUES (?, ?)', values)
    c.close()
    # Load into pandas
    print(load_sql.__doc__)
    t1 = pd.read_sql_query("SELECT * FROM table1", conn)
    print(t1.head())

def view():
    """3. Můžeme snadno vyfiltrovat řádky:"""

    t1 = pd.read_csv(datafile1)

    print(view.__doc__)

    print('t1[t1.index != 2]')
    print( t1[t1.index != 2] )

    print('t1.drop(t1.index[[2,3]])')
    print( t1.drop(t1.index[[2,3]]) )

def transform():
    """4. Transformování sloupce či řádku."""

    t1 = pd.read_csv(datafile1)

    print(transform.__doc__)

    print("Apply labda:")
    t1['ab'] = t1['a']+t1['b']
    t1['c+c'] = t1['c']+t1['c']
    t1['addone'] = t1['c'].apply(lambda x: x+1)
    t1['pow2'] = t1['c'].apply(lambda x: int(math.pow(x,2)))
    t1['pipe'] = t1['a'].apply(lambda x: x+"|")
    print(t1)

    print("Append one dataframe to another:")
    print(t1.append(t1))

def main():
    print(__doc__)

    load_csv()
    load_sql()
    view()
    transform()

if __name__ == '__main__':
    main()
