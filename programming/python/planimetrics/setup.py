#!/usr/bin/env python3

from setuptools import find_packages, setup

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries'
]

params = {
    'name':             "planimetrics",
    'version':          "0.1.0",
    'description':      '',
    'keywords':         'planimetrics, geometry, math',
    'author':           'Ondřej Profant',
    'url':              'https://www.github.com',
    'license':          'GPLv3',
    'packages':         find_packages(exclude=['tests', 'tests.*']),
    #'test_suite':       'tests',
    'classifiers':      CLASSIFIERS,
}

setup(**params)