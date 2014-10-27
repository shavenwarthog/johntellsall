
.. Tricking out Linux Networking slides file, created by
   hieroglyph-quickstart on Wed Aug 20 15:12:52 2014.


Tricking out Linux Networking
=============================


ME
====

   - Senior dev/server consultant; DevOps
   - 20 years experience with Python
   - john@johntellsall.com


THEME
=====

Linux networking is cool, by understanding details you can do useful
tricks

- survey
- wrong
- tricks
- awesome

SECTION: future (Docker, Cgroups) and past (mmap IPC; last month)

* audience: sr engineer, CTO, DevOps

Won't cover: (kernel) queues, RT signals, ipfilter subsystem; also
TIPC, inotify



- _connected_ datagram sockets (Linux only?)



socket address families (AF)
----------------------------

=================== ==============================
**AF_INET**             IPv4 Internet protocols
AF_INET6            IPv6 Internet protocols
**AF_NETLINK**          Kernel user interface device
AF_PACKET           Low level packet interface
**AF_UNIX**   			Local communication
=================== ==============================


.. note::

   AF_APPLETALK        AppleTalk
   AF_ATMPVC           Access to raw ATM PVCs
   AF_AX25             Amateur radio AX
   AF_IPX              IPX - Novell protocols
   AF_X25              ITU-T X.25




"socket" creates a record in the kernel, which talks to a driver



☃
=

Questions?
================

.. figure:: /_static/john-bold.jpg
   :class: fill

   john@johntellsall.com

