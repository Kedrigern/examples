#!/usr/bin/env python3

__version__ = "v1.0.0"
__author__ = "Ondřej Profant"
__description__ = """
"""

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def psp_table_len(url, selector):
  soup = BeautifulSoup(urlopen(url), "lxml")

  table = soup.find('div', {'class': selector}).find('table')
  trs = table.findAll('tr')
  result = len(trs) -1
  return(result)

def zpravodaj():
  url = "https://www.psp.cz/sqw/tisky.sqw?sn=6526"  
  return psp_table_len(url, 'search-results')

def pn():
  url = "https://www.psp.cz/sqw/ppn.sqw?id=6526"
  return psp_table_len(url, 'section')

def predkladatel():
  url = "https://www.psp.cz/sqw/tisky.sqw?nz=6526"
  soup = BeautifulSoup(urlopen(url), "lxml")

  div = soup.find('div', {'class': 'search-results'})

  pat = r'Celkem nalezeno (\d+)'
  return int(re.search(pat, div.text).groups()[0])

def hlasovani():
  url = "https://www.psp.cz/sqw/pstat.sqw?o=8&id=6526&id_posl=1664"
  soup = BeautifulSoup(urlopen(url), "lxml")

  tds = soup.find('div', {'class': 'job-list'}).table.tr.findAll('td')
  pat = r'(\d+)'
  return re.search(pat, tds[1].text).groups()[0]


print("zpravodaj", zpravodaj())
print("pn", pn())
print("predkladatel", predkladatel())
print("hlasoval", hlasovani())