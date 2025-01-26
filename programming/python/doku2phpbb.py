#!/usr/bin/env python3
"""
Converts dokuwiki syntax into phpbb or markdown syntax
"""

__author__ = "Ondřej Profat"
__version__ = "v0.5.0"

import os
import re
import sys
import argparse
from pprint import pprint

test_links = [
"[[http://example.com|example]]",
"[[https://www.example.com/user/|example]]",
"[[https://www.example.com|example web]]",
"[[https://www.example.com|ěščřžýáíé]]",
"[[https://www.example.com/+|ěščřžýáíé+]]",
"""
Lorem ipsum [[http://example.com/user/|example user]] et dolorem
Lorem ipsum [[http://www.example.com/|example]] et dolorem
"""]

test_headings = [
"== heading ==",
"== heading 2 ==",
"""
== heading ==
lorem ipsum
"""
]

test_bullets = [
"  * první odrážka",
"""
  * a)
  * b)
  * c)
"""
]

complete_example = ["""
== heading ==

Lorem ipsum [[http://example.com|example]].

  * a)
  * b)
  * c)
"""]

re_link = {
    'r': {
        'md': r'\[(?P<name>[\w\ +]+)\]\((?P<url>http[s]?://[\w\./+-]*)\)',
        'doku': r'\[\[(?P<url>http[s]?://[\w\./+-]*)\|(?P<name>[\w\ +]+)\]\]'
    },
    'w': {
        'md': r'[\g<name>](\g<url>)',
        'doku': r'[[\g<url>|\g<name>]]',
        'phpbb': r'[url=\g<url>]\g<name>[/url]'

    }
}
re_bullet = {
    'r': {
        'doku': r'^(  \*)'
    },
    'w': {
        'md': r' *',
        'doku': r'  *',
        'phpbb': r'[*]'
    }
}
re_headings = {
    'r': {
        'doku': r'^[ ]*==([\w ]*)==[ ]*$'
    },
    'w': {
        'md': r'## \1',
        'doku': r'== \1 ==',
        'phpbb': r'[b]\1[/b]'
    }
}

def convert(text, frm='doku', to='phpbb'):
    """Converts string by defined regexps"""
    links = re.sub(re_link['r'][frm], re_link['w'][to], text)
    bullet = re.sub(re_bullet['r'][frm], re_bullet['w'][to], links, flags=re.MULTILINE)
    return re.sub(re_headings['r'][frm], re_headings['w'][to], bullet, flags=re.MULTILINE)

try:
    filename = sys.argv[1]
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            print(convert(f.read()))
except:
    print("No file")
    for s in test_links + test_headings + test_headings + complete_example:
        print("~~~ Test string:")
        print(s)
        print("~~~ New string:")
        print(convert(s))
        print("~~~~~~~~~~~~~~~")
