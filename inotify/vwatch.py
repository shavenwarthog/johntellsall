#!/usr/bin/env python

'''
vwatch.py -- print filesystem events in tree of files
'''

import os, sys

import inotifyx


def find_dirs(topdir):
    yield topdir
    for root, dirs, _files in os.walk(os.path.expanduser(topdir)):
        for mydir in dirs:
            yield os.path.join(root, mydir)


def add_watch_dirs(topdir, fd, mask):
    '''
    add inotify watch for every directory in tree starting at 'topdir'
    '''
    try:
        path = None
        return dict( (
            (inotifyx.add_watch(fd, path, mask), path)
            for path in find_dirs(topdir)
        ) )
    except IOError, exc:
        sys.exit('{}: {}'.format(path, exc))


def scan(topdir):
    '''
    print filesystem events for tree of files
    '''
    fd = inotifyx.init()

    mask = inotifyx.IN_MODIFY | inotifyx.IN_CLOSE_WRITE
    if 0:
        mask = inotifyx.IN_ALL_EVENTS

    wd_to_path = add_watch_dirs(
        topdir=topdir,
        fd=fd,
        mask=mask,
        )

    try:
        oldpath = None
        while True:
            for event in inotifyx.get_events(fd):
                path = os.path.join(
                    wd_to_path[event.wd],
                    event.name if event.name else '',
                    )

                parts = [ event.get_mask_description() ]
                parts = [ word.replace('IN_ALL_EVENTS|', '')
                          for word in parts
                          ]

                if path != oldpath:
                    print path
                oldpath = path
                print '\t', ' '.join(parts)

    except KeyboardInterrupt:
        pass
    finally:
        os.close(fd)


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: {} (topdir)'.format(sys.argv[0]))

    scan(sys.argv[1])


if __name__ == "__main__":
    main()
