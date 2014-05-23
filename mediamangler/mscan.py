#!/usr/bin/env python

'''
mscan.py -- scan media files, print info on each
'''

import os, sys


MIN_SIZE = 100 * 1024


def scan_files(topdir):
    for mydir, _dirs, names in os.walk(topdir):
        for name, path in ( (name, os.path.join(mydir, name))
                            for name in names
                       ):
            yield name, path


def get_meta(filename):
    from hachoir_core.error import HachoirError
    from hachoir_core.cmd_line import unicodeFilename
    from hachoir_parser import createParser
    from hachoir_core.tools import makePrintable
    from hachoir_metadata import extractMetadata
    from hachoir_core.i18n import getTerminalCharset
    filename, realname = unicodeFilename(filename), filename
    parser = createParser(filename, realname)
    if not parser:
        print >>sys.stderr, "{}: Unable to parse file".format(filename)
        return None

    return extractMetadata(parser)
    # except HachoirError, err:
    #     print "Metadata extraction error: %s" % unicode(err)
    #     metadata = None
    # if not metadata:
    #     print "Unable to extract metadata"
    #     exit(1)

    # text = metadata.exportPlaintext()
    # charset = getTerminalCharset()
    # for line in text:
    #     print makePrintable(line, charset)


def main(topdir):
    def is_boring(name, path):
        return ( name.startswith('.') or 
                 os.path.getsize(path) < MIN_SIZE
                 )
    for name,path in scan_files(topdir): # TODO: use ifilter
        if is_boring(name,path):
            continue
        print path

        meta = get_meta(path)
        # print meta
        

if __name__=='__main__':
    main( os.path.expanduser(sys.argv[1]) )


