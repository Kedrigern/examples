#!/usr/bin/env python3

"""
Python3 and SQLite examples:
    - datatypes
    - select and subselects
    - parse csv
    - insert many
    - named placeholders
Database is in memory.

Data about czech municipalities are from MVČR.
"""

import csv
import sqlite3
import datetime

def load(file_obce, file_orp, connection):
    c = connection.cursor()
    c.execute('''CREATE TABLE obce (
        id int,
        name varchar,   -- název obce bez bílých znaků okolo
        orp_id int,     -- id obce s rozšířenou působností (orp) z tabulky orp
        okres_id int,   -- id okresu
        typ varchar(1), -- hodnoty: O, M, T, U, S, H
        csu_id int,
        pcd_id int
    ) ''')

    with open(file_obce) as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        for row in reader:
            val7 = int(row[7]) if row[7] else None
            values = (int(row[0]), row[1].strip(), int(row[2]), int(row[4]), row[5], int(row[6]), val7)
            c.execute('INSERT INTO obce VALUES (?, ?, ?, ?, ?, ?, ?)', values)

    c.execute('''CREATE TABLE orp (
        id int,     
        name varchar,
        csu_id int,
        typ varchar(1),
        okres_id int
    ) ''')

    with open(file_orp) as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        for row in reader:
            id =     int(row[0]) if row[0].strip() else None
            csu_id = int(row[2]) if row[2].strip() else None
            okres =  int(row[4]) if row[4].strip() else None
            values = (id, row[1].strip(), csu_id, row[3].strip(), okres)

            c.execute('INSERT INTO orp VALUES (?, ?, ?, ?, ?)', values)

    c.execute('''CREATE TABLE people (
        name varchar,
        salary int,
        born date
    ) ''')
    people = [
        ('Ala',  20800, '1990-09-20'),
        ('Alan', 21600, '1989-10-20'),
        ('Anna', 22500, '1988-11-15'),
        ('Lala', 23500, '1987-12-01'),
        ('Leo',  22100, '1986-05-13')
    ]
    c.executemany('INSERT INTO people VALUES (?,?,?)', people)

    more_people = [
        {'name': 'Jana', 'salary': 22100, 'born': datetime.date(1990, 3, 3)},
        {'name': 'Dana', 'salary': 22100, 'born': datetime.date(1990, 3, 3)}
    ]
    c.executemany('INSERT INTO people VALUES (:name, :salary, :born)', more_people)
    connection.commit()

def examples(connection):
    c = connection.cursor()

    count = c.execute('SELECT count(*) FROM obce').fetchone()
    print("Počet obcí: %d\n" % count)

    obce = c.execute("SELECT * FROM obce WHERE name LIKE 'vejvanov%'").fetchall()
    print("Obce jejiž jméno začíná vejvanov\n", obce)

    answer = c.execute("SELECT DISTINCT(typ) FROM obce;")
    print("Typy obcí:\n", [t[0] for t in answer.fetchall()])

    answer = c.execute("SELECT name FROM obce WHERE orp_id IN (SELECT id FROM orp WHERE name = 'Černošice' or name = 'Beroun' )")
    print("Obce jejiž ORP jsou Černošice nebo Beroun:\n", [r[0] for r in answer.fetchall()])


    answer = c.execute("SELECT * FROM people WHERE name LIKE '_ana'").fetchall()
    print("Jména _ana:\n", answer)

    answer = c.execute("SELECT * FROM people WHERE born BETWEEN '1987-01-01' AND '1989-01-01'").fetchall()
    print("Narozeni 87-88:\n", answer)

    connection.commit()

def main():
    conn = sqlite3.connect(':memory:')
    load('obce.csv', 'orp.csv', conn)
    examples(conn)
    conn.close()

if __name__ == '__main__':
    main()
