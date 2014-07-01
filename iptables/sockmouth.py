#!/usr/bin/env python

'''
sockmouth.py -- process kernel info about sockets
'''
# INSTALL
#	sudo iptables -A INPUT -p TCP --dport 80 -j ULOG --ulog-nlgroup 2
#
# REFERENCE
# - https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html#ULOGTARGET


import re
from pprint import pprint

from pyroute2 import netlink


def format_bytes(raw_str):
    rvals = ( 
        int(rhex, 16)
        for rhex in raw_str
    )
    rstring = ''.join( ( 
        chr(rval) if 32 <= rval < 127 else '.'
        for rval in rvals
    ) )
    return re.sub(r'\.+', '.', rstring)


# pylint: disable=E1101
def mnetlink():
    class MyNetlink(netlink.client.Netlink):
        family = netlink.generic.NETLINK_NFLOG 
        groups = 2

    con = MyNetlink(
        debug=True, 
        )
    con.monitor()               

    while True:
        for raw in con.get():
            data = raw.pop('header')
            if raw:
                print('WEIRD: {}'.format(raw))
            print( format_bytes( data.pop('raw').split(':') ) )
            print '\t', data 
            

if __name__=='__main__':
    mnetlink()
