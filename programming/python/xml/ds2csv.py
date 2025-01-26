#!/usr/bin/env python3
# Načtení seznamu datových schránek
# Zdroj dat: https://www.mojedatovaschranka.cz/sds/welcome.do?part=opendata

import csv
from lxml import etree as ET

sample = """
<list xmlns="http://seznam.gov.cz/ovm/datafile/seznam_ds/v1">
    <box>
        <id>6hv7j6g</id>
        <type>FO</type>
        <subtype>40</subtype>
        <name>
            <person>
                <firstName>Mahmoud</firstName>
                <lastName>Ababneh</lastName>
            </person>
            <tradeName></tradeName>
        </name>
        <ico></ico>
        <address>
            <city>Hustopeče</city>
            <district></district>
            <street>Mírová</street>
            <cp>1104</cp>
            <co>10</co>
            <ce></ce>
            <zip>69301</zip>
            <state>CZ</state>
            <fullAddress></fullAddress>
        </address>
        <pdz>true</pdz>
        <ovm>false</ovm>
        <hierarchy>
            <isMaster>true</isMaster>
        </hierarchy>
        <idOVM></idOVM>
    </box>
</list>
"""
test = True

def parseDSxml(root):
  ns = root.nsmap
  boxes = root.findall('box', ns)
  result = []
  for box in boxes:
    result.append([
      box.find('id', ns).text,
      box.find('type', ns).text,
      box.find('name/person/firstName', ns).text, 
      box.find('name/person/lastName', ns).text])
  return result
  
def export(res):
  with open('ds.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["id", "type", "firstname", "lastname"])
    for r in res:
      writer.writerow(r)

if test:
  root = ET.fromstring(sample)
else:
  fp = "./datafile-seznam_ds_fo-20181205182004.xml"
  tree = ET.parse(fp)
  root = tree.getroot()

res = parseDSxml(root)
export(res)