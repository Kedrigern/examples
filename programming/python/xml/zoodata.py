#!/usr/bin/env python3

"""Example for opendata.praha.eu"""

__author__ = "Ondrej Profant"
__version__ = "1.0"

from urllib.request import urlopen
from json import loads
from pprint import pprint

urls = {
    "akce": "https://www.zoopraha.cz/_api/json/?action=akcezoo&type=rel",
    "adopce": "https://www.zoopraha.cz/_api/json/?action=adopcezvirata&type=rel",
    "lexikon": "https://www.zoopraha.cz/_api/json/?action=lexikoncelek&type=rel"
}

for k, v in urls.items():
   response = urlopen(v) 
   text = response.read().decode("utf-8-sig")
   json = loads(text)

   print(k, ":")
   pprint(json[0])
    

