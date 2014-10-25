#!/usr/bin/env python

from pyroute2 import IPDB
# local network settings
ip = IPDB()
# # create bridge and add ports and addresses
# # transaction will be started with `with` statement
# # and will be committed at the end of the block
# with ip.create(kind='bridge', ifname='rhev') as i:
#     i.add_port(ip.interfaces.em1)
#     i.add_port(ip.interfaces.em2)
#     i.add_ip('10.0.0.2/24')

