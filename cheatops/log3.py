#!/usr/bin/env python

'''
log3.py -- watch external server connections
'''
# pylint: disable=W0232

import argparse, os, subprocess, sys

from pyroute2 import netlink


CMD_LIST = 'sudo iptables -L'
CMD_SETUP = 'sudo iptables -A INPUT -p TCP --dport {port} -j ULOG --ulog-nlgroup {group_id}'


class NflogNetlink(netlink.client.Netlink):
    family = netlink.generic.NETLINK_NFLOG
    groups = None               # must override


def format_nflog(rec):
    '''
    zap boring fields
    '''
    out = dict(rec)             # copy
    for field in 'error pid flags offset sequence_number'.split():
        if field in rec and not rec.get(field):
            del out[field]
    return out


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


def cmd_install(args):
    group_str = 'nlgroup {}'.format(args.nlgroup)
    for line in subprocess.check_output(
            CMD_LIST, shell=True).split('\n'):
        if group_str in line:
            print 'Already installed'
            print '\t',line
            return
    blam

    
def cmd_watch(args):            # pylint: disable=W0613
    if os.geteuid():
        sys.exit('must be root')

    print '\tExample: curl localhost'

    NflogNetlink.groups = args.nlgroup # XX: side effects
    con = NflogNetlink(
        debug=True,
    )
    con.monitor()               # pylint: disable=E1101

    while True:
        for raw in con.get():   # pylint: disable=E1101
            data = raw.pop('header')
            print len(data['raw'])     # bytes
            print '\t', format_nflog(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'commands', type=str, nargs='+')
    parser.add_argument(
        '--nlgroup', type=int, default=2)
    # parser.add_argument(
    #     '--inet', dest='linktype', const='inet',
    #     action='store_const')

    args = parser.parse_args()
    for command in args.commands:
        cfunc = globals().get('cmd_{}'.format(command))
        if cfunc:
            cfunc(args)
        else:
            sys.exit('{}: no such command'.format(command))


if __name__=='__main__':
    main()
