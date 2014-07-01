#!/usr/bin/env python

# pylint: disable=E1101,W0232

import argparse, os, re, sys

from pyroute2 import netlink


CMD_SETUP = 'sudo iptables -A INPUT -p TCP --dport 80 -j ULOG --ulog-nlgroup 2'
CMD_LIST = 'sudo iptables -L'


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


def format_nflog(rec):
    '''
    zap boring fields
    '''
    out = dict(rec)             # copy
    for field in 'error pid flags offset sequence_number'.split():
        if field in rec and not rec.get(field):
            del out[field]
    return out


# ::::::::::::::::::::::::::::::::::::::::::::::::::

# TODO: simplify

class nflogNetlink(netlink.client.Netlink):
    family = netlink.generic.NETLINK_NFLOG 
    groups = 2

class inetNetlink(netlink.client.Netlink):
    family = netlink.generic.NETLINK_INET_DIAG


def cmd_watch(args):            # pylint: disable=W0613
    print 'Watching {} messages'.format(args.linktype)
    if args.linktype == 'nflog':
        print '\tExample: curl localhost'

    con = globals().get('{}Netlink'.format(args.linktype))(
        debug=True, 
    )
    con.monitor()               

    while True:
        for raw in con.get():
            data = raw.pop('header')
            if raw:
                print('WEIRD: {}'.format(raw))
            print( format_bytes( data.pop('raw').split(':') ) )
            print '\t', format_nflog(data)
            

def cmd_list(args):             # pylint: disable=W0613
    err = os.system(CMD_LIST)
    if err:
        sys.exit(1)


def cmd_setup(args):
    err = os.system(CMD_SETUP)
    if err:
        sys.exit(1)


# ::::::::::::::::::::::::::::::::::::::::::::::::::

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'commands', type=str, nargs='+')
    parser.add_argument(
        '--nflog', dest='linktype', const='nflog',
        default='nflog',
        action='store_const')
    parser.add_argument(
        '--inet', dest='linktype', const='inet',
        action='store_const')

    args = parser.parse_args()
    for command in args.commands:
        cfunc = globals().get('cmd_{}'.format(command))
        if cfunc:
            cfunc(args)
        else:
            sys.exit('{}: no such command'.format(command))


if __name__=='__main__':
    main()
