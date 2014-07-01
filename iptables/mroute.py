#!/usr/bin/env python

import argparse, os, sys

from pyroute2 import IPRoute


CMD_SETUP = 'sudo iptables -A INPUT -p TCP --dport 80 -j ULOG --ulog-nlgroup 2'
CMD_LIST = 'sudo iptables -L'


def cmd_watch(args):
    class MyNetlink(netlink.client.Netlink):
        family = netlink.generic.NETLINK_NFLOG 
        groups = 2

    con = MyNetlink(
        debug=True, 
        )
    con.monitor()               

    while True:
        for raw in con.get():
            pprint(raw)


def cmd_list(args):
    err = os.system(CMD_LIST)
    if err:
        sys.exit(1)


def cmd_setup(args):
    err = os.system(CMD_SETUP)
    if err:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('commands', type=str, nargs='+')
    parser.add_argument('--list', '-L', dest='cmd_list', 
                        action='store_true')

    args = parser.parse_args()
    for command in args.commands:
        cfunc = globals().get('cmd_{}'.format(command))
        if cfunc:
            cfunc(args)
        else:
            sys.exit('{}: no such command'.format(command))


if __name__=='__main__':
    main()
