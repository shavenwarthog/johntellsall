SURVEY
============================

what types of IPC are there?


TCP sockets
-----------

- address: Internet, IP+port
- reliable stream of bytes


UDP socket
-----------

- address: Internet, IP+port
- small packets (0.5KB - 63KB)
- fast, low latency
- unreliable: drops, dups, reordering
- feature: multicast!


UDP Multicast
-------------

- any number producers and consumers
- unreliable: reorder, dropped, duplicate

TODO


Unix sockets
------------

- address: unnamed, path, or "abstract namespace"
- same machine, bidirectional
- byte streams, packets, and seq packets
* fast!
* low latency!
 

Pipes
named pipes
shared memory
queues
signals

LATER: ICMP -- Redirect!

