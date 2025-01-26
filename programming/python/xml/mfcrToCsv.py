#!/usr/bin/env python3

import csv
import lxml.etree as ET

url = "https://downloads.statnipokladna.cz/ciselniky/RISRE0017_C001_20180302_PVS.XML"
fp = "PVS.XML"
want = [
    'rrkd:Kapitola',
    'rrkd:StrukturaPrijmovaVydajova',
    'rrkd:Text/rrkd:Nazev',
    'rrkd:Text/rrkd:Popis',
    'rrkd:Text/rrkd:PopisDlouhy'
]

def parsePVSxml(root):
    ns = root.nsmap
    polozky = root.findall('rrkd:StrukturaPrijmovaVydajova/rrkd:Polozka', ns)
    result = []
    for pol in polozky:
        tmpResult = []
        for w in want:
            tmp = pol.find(w, ns)
            tmpResult.append(tmp.text)
        result.append(tmpResult)
    return result

def export(res):
    with open('pvs.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(want)
        for r in res:
            writer.writerow(r)

tree = ET.parse(fp)
root = tree.getroot()
res = parsePVSxml(root)
export(res)