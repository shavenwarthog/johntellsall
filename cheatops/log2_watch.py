#!/usr/bin/env python

'''
log2_watch.py -- calc number of outstanding Apache requests

INSTALL:
Apache2 config:
	ForensicLog "|log2_watch.py"

WARNING:
When running under standard Apache2, runs as root!
'''

import sys, threading, time


def get_log(changed_ev, counter_obj):
    while True:
        line = sys.stdin.readline()
        if line.startswith('+'):
            counter_obj['count'] += 1
            changed_ev.set()
        elif line.startswith('-'):
            counter_obj['count'] -= 1
            changed_ev.set()


def start_timer(changed_ev, counter_obj):
    threading.Timer(1.0, write_count, (changed_ev, counter_obj)).start()

def write_count(changed_ev, counter_obj):
    start_timer(changed_ev, counter_obj)
    if not changed_ev.is_set():
        return
    changed_ev.clear()
    print time.ctime(), counter_obj['count']


def main():
    changed_ev = threading.Event()
    counter_obj = dict(count=0)

    start_timer(changed_ev, counter_obj)
    threads = [ 
        threading.Thread(
            target=get_log, args=(changed_ev, counter_obj)
            ),
        ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__=='__main__':
    main()
