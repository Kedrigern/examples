#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:41:57 2016
Web scraper of zoo list of animals for adoption
@author: Piter de Vries, Ondřej Profant

Extract data from from multiple same structured html tables into one csv
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = "https://www.zoopraha.cz/jak-pomoci/adopce/seznam-zvirat-pro-adopci"
infile = "in.html"
output = "zoo_funds.csv"

html = urlopen(url)
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")

with open(output, 'w', encoding='utf-8') as fd:
    spamwriter = csv.writer(fd, delimiter=',')
    for table in tables:    
        for row in table.find_all("tr")[1:]:
            columns = [td for td in row.find_all("td")]
            a = columns[3].find_all('a')
            a1 = str(a[0]['href'])
            a2 = str(a[1]['href'])        
            data = [ 
                str(columns[0].get_text()),
                str(columns[1].get_text()),
                str(columns[2].get_text()),
                a1, a2]
            print(data)    
            spamwriter.writerow(data)

    
