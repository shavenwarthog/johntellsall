#!/usr/bin/env python

'''
log4.py -- watch external server connections via NFQUEUE

Caveat: must 'accept' each packet or Bad Things Happen.

INSTALL:
pip install NetfilterQueue

SETUP:
sudo iptables -I INPUT -p TCP --dport 80 -j NFQUEUE --queue-num 1
'''
# pylint: disable=W0232

import argparse, os, re, subprocess, sys

from netfilterqueue import NetfilterQueue




# CMD_LIST = 'sudo iptables -L'
# CMD_SETUP = 'sudo iptables -A INPUT -p TCP --dport {port} -j ULOG --ulog-nlgroup {group_id}'


# class NflogNetlink(netlink.client.Netlink):
#     family = netlink.generic.NETLINK_NFLOG
#     groups = None               # must override


# def format_nflog(rec):
#     '''
#     zap boring fields
#     '''
#     out = dict(rec)             # copy
#     for field in 'error pid flags offset sequence_number'.split():
#         if field in rec and not rec.get(field):
#             del out[field]
#     return out


# # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# def cmd_install(args):
#     group_str = 'nlgroup {}'.format(args.nlgroup)
#     for line in subprocess.check_output(
#             CMD_LIST, shell=True).split('\n'):
#         if group_str in line:
#             print 'Already installed'
#             print '\t',line
#             return
#     blam

    
# must be root
def cmd_watch(args):            # pylint: disable=W0613
    print '\tExample: curl localhost'

    def print_and_accept(pkt):
        pkt.accept()
        data = pkt.get_payload()
        m = re.compile('(GET|POST)(.*)', re.DOTALL).search(data)
        if not m:
            print '??',''.join( re.findall('[ -_]+', data) )
            return
        print m.group(1) + m.group(2)

    nfqueue = NetfilterQueue()
    nfqueue.bind(args.nfqueue, print_and_accept)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'commands', type=str, nargs='+')
    parser.add_argument(
        '--nfqueue', type=int, default=1)

    args = parser.parse_args()
    for command in args.commands:
        cfunc = globals().get('cmd_{}'.format(command))
        if cfunc:
            cfunc(args)
        else:
            sys.exit('{}: no such command'.format(command))


if __name__=='__main__':
    main()
