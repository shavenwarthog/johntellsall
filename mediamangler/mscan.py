#!/usr/bin/env python

'''
mscan.py -- scan media files, print info on each
'''

import os, sys

import mutagen


MIN_SIZE = 100 * 1024


def scan_files(topdir):
    for mydir, _dirs, names in os.walk(topdir):
        for name, path in ( (name, os.path.join(mydir, name))
                            for name in names
                       ):
            yield name, path


def main(topdir):
    def is_boring(name, path):
        return ( name.startswith('.') or 
                 os.path.getsize(path) < MIN_SIZE
                 )
    for name,path in scan_files(topdir): # TODO: use ifilter
        if is_boring(name,path):
            continue
        print path

        meta = None
        try:
            meta = mutagen.File(path, easy=True)
        except mutagen.mp4.MP4StreamInfoError:
            pass
        try:
            print '\t{artist}\t{album}'.format(**meta)
        except KeyError:
            print '??', meta


if __name__=='__main__':
    main( os.path.expanduser(sys.argv[1]) )

# print(
#     '\n'.join( scan_files( os.path.expanduser(sys.argv[1]) )
#                )
#     )


