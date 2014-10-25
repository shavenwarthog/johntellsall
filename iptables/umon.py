#!/usr/bin/env python

from pprint import pprint

from pyroute2 import IPRoute, IPRSocket
from pyroute2 import netlink

def mroute():
    ip = IPRoute() # family = NETLINK_ROUTE "Receives routing and link
    # updates and may be used to modify the routing tables"
    ip.monitor()

    while True:
        for raw in ip.get():
            print '{event:10} {attrs}'.format(**raw)

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
            pprint(raw)



# if __name__=='__main__':
#     mnetlink()
