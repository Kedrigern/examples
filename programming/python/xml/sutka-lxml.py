#!/usr/bin/env python3

__version__ = "v1.0.0"
__author__ = "Ondřej Profant"
__description__ = """
Parse availability and count of visitors in aquapark Šutka: sutka.eu
"""

import re
import string
from lxml import html

url = "http://www.sutka.eu"
tree = html.parse(url)

div = tree.xpath("//div[@id='header-info_availability']")[0]
availability_text = div.xpath("p[2]/text()")[0].strip('\n\t ')
apattern = '^\w*: (\d+(.\d+)*)%$'
availability_raw = re.search(apattern, availability_text).groups()[0]

visitors_text = div.xpath("p[1]/text()")[0].strip('\n\t ')
vpattern = '\w+ \w+ \w+: (\d+) \((\w+)\), (\d+) \((\w+)\)'
visitors_arr = re.search(vpattern, visitors_text).groups()

print(availability_raw, '%', visitors_arr[1], visitors_arr[0], ':', visitors_arr[3], ':', visitors_arr[2])
