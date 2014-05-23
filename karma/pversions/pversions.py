#!/usr/bin/env python

'''
pversions.py -- search for package version from PyPi
'''
# adapted from pip.commands.SearchCommand

import sys, xmlrpclib

pnames = sys.argv[1:]
if not pnames:
    sys.exit('Usage: pversions (packagename)...')

pypi = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
for packagename in (pname.lower() for pname in pnames):
    print packagename,':'
    exact_hits = (
        hit for hit in pypi.search({'name': packagename})
        if hit['name'].lower() == packagename
    )
    print ', '.join( (hit['version'] for hit in exact_hits) )

