#!/usr/bin/env python

import os, sys
from itertools import takewhile


def print_indent(lines):
    for line in lines:
        line = line.rstrip()
        print "    ",line

for path in sys.argv[1:]:
    suffix = os.path.splitext(path)[-1]
    if suffix == '.py':
        print path
        print '----------------'
        print
        print '.. code-block:: python'
        print
        source = open(path)
        skip_aux = takewhile(lambda line: 'AUX' not in line, source)
        print_indent( skip_aux )
        print
        
    elif suffix == '.out':
        print '::'
        print
        # output = open(path)subprocess.check_output(
        #     ['python', path],
        #     ).split('\n')
        print_indent( open(path) )
    else:
        sys.exit('{}: Unknown suffix: {}'.format(path, suffix))
