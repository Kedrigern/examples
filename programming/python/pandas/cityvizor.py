#!/usr/bin/env python3

import sys
import pandas as pd

def main():
    prefix = 'data/p7-2016'
    names = ["DOKLAD_ROK","DOKLAD_DATUM","DOKLAD_AGENDA","DOKLAD_CISLO","ORGANIZACE","ORGANIZACE_NAZEV","ORJ","ORJ_NAZEV","PARAGRAF","PARAGRAF_NAZEV","POLOZKA","POLOZKA_NAZEV","SUBJEKT_IC","SUBJEKT_NAZEV","CASTKA_MD","CASTKA_DAL","POZNAMKA"]
    to_del = ['DOKLAD_ROK', 'ORGANIZACE_NAZEV', 'ORJ', 'ORJ_NAZEV', 'PARAGRAF_NAZEV', 'DOKLAD_CISLO', 'POLOZKA_NAZEV']
    to_use = ["DOKLAD_ROK", "DOKLAD_DATUM"]

    sr = pd.read_csv(prefix + '/SR.csv', sep=';', header=1, names=names, usecols=to_use)
    print(sr.head())
    #ru = pd.read_csv(prefix + '/RU.csv', sep=';')
    #sk = pd.read_csv(prefix + '/SK.csv', sep=';')

    #merged = sr.append([ru, sk], ignore_index=True)
    #merged.set_index(inplace=True)
    #merged.drop(to_del, axis=1, inplace=True)
    #print(merged.head())



if __name__ == '__main__':
    main()
