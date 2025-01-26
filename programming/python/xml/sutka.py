#!/usr/bin/env python3

__version__ = "v2.0.0"
__author__ = "Ondřej Profant"
__description__ = """
Parse availability and count of visitors in aquapark Šutka: sutka.eu
"""

import re
import string
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.sutka.eu"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

div = soup.find('div', {'id': 'header-info_availability'})

visitors_text = div.find('p').text # e.g. Aktuální počet návštěvníků: 45 (Bazén), 0 (Aquapark)
obsazenost_text = div.findAll('p')[1].text # Obsazenost: 11% 

vpattern = r'\w+ \w+ \w+: (\d+) \((\w+)\), (\d+) \((\w+)\)'
apattern = r'\w*: (\d+[.\d+]*)%'

(bazen, _, aquapark, _) = re.search(vpattern, visitors_text ).groups()
procent = re.search(apattern, obsazenost_text ).groups()[0]

print('Bazén: %s, Aquapark: %s, procent: %s%%' % (bazen, aquapark, procent))

