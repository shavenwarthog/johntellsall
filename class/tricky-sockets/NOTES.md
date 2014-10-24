traditional TCP sockets

UDP sockets

UDP multicast

- any number producers and consumers
- unreliable: reorder, dropped, duplicate


AF_UNIX SOCK_DGRAM

AF_UNIX

AF_UNIX, AF_LOCAL   Local communication              unix(7)
AF_INET             IPv4 Internet protocols          ip(7)
AF_INET6            IPv6 Internet protocols          ipv6(7)
AF_IPX              IPX - Novell protocols
AF_NETLINK          Kernel user interface device     netlink(7)
AF_X25              ITU-T X.25 / ISO-8208 protocol   x25(7)
AF_AX25             Amateur radio AX.25 protocol
AF_ATMPVC           Access to raw ATM PVCs
AF_APPLETALK        AppleTalk                        ddp(7)
AF_PACKET           Low level packet interface       packet(7)

SOCK_STREAM     Provides sequenced, reliable, two-way, connection-
based byte streams.  An out-of-band data transmission
mechanism may be supported.

SOCK_DGRAM      Supports datagrams (connectionless, unreliable
messages of a fixed maximum length).

SOCK_SEQPACKET  Provides a sequenced, reliable, two-way connection-
based data transmission path for datagrams of fixed
maximum length; a consumer is required to read an
entire packet with each input system call.

SOCK_RAW        Provides raw network protocol access.

SOCK_RDM        Provides a reliable datagram layer that does not
guarantee ordering.

http://man7.org/linux/man-pages/man7/unix.7.html

The AF_UNIX (also known as AF_LOCAL) socket family is used to
communicate between processes on the same machine efficiently.
Traditionally, UNIX domain sockets can be either unnamed, or bound to
a filesystem pathname (marked as being of type socket).  Linux also
supports an abstract namespace which is independent of the
filesystem.

Valid types are: SOCK_STREAM, for a stream-oriented socket and
SOCK_DGRAM, for a datagram-oriented socket that preserves message
boundaries (as on most UNIX implementations, UNIX domain datagram
sockets are always reliable and don't reorder datagrams); and (since
Linux 2.6.4) SOCK_SEQPACKET, for a connection-oriented socket that
preserves message boundaries and delivers messages in the order that
they were sent.

UNIX domain sockets support passing file descriptors or process
credentials to other processes using ancillary data.



TIP: SO_REUSEADDR

http://stackoverflow.com/questions/3324619/unix-domain-socket-using-datagram-communication-between-one-server-process-and

"However, unix domain datagram sockets are different. In fact, the write() will actually block if the client's receive buffer is full rather than drop the packet. . This makes unix domain datagram sockets much superior to UDP for IPC because UDP will most certainly drop packets when under load, even on localhost. "

AF_UNIX SOCK_STREAM

AF_DBUS -- multicast Unix domain sockets, aka multicast pipes!

https://lkml.org/lkml/2012/2/20/208



References
==========

https://wiki.python.org/moin/UdpCommunication

sudo apt-get install python-examples




* audience: sr engineer, CTO, DevOps

* concept doesn't always match implementation 

what is a file?
	seekable collection of persistent bytes
how do you get one?
	ask kernel, get handle
what can you do with it?
	close, read/write, fctrl
"disk file": really?
	/dev/null, /proc/fd, named pipes!
=> concept doesn't match

what is a socket?
	stream of bytes, bidirectional, multi-machine
how do you get one?
	ask kernel, get handle
what can you do with it?
	close, ioctl?, send/recv
"stream of bytes": really?
	mostly; what about UDP; 
=> concept doesn't match
(default TCP settings are for file transfer, want to change settings for HTTP-ish traffic, matters if you're internet-facing vs LAN; bufferbloat)

namespaces
- socket: IP? multiple IPs? IPv6? TIPC address?
- filesystem
- in-kernel socket space!
- cool ipfilter tricks, out of scope

* kernel provides (file like) abstractions over *lots* of different
services, in different namespaces.  *
* actual implementation differs!
Ex: "stream of bytes" vs send fd to unrelated proc over X socket
Ex: tell kernel to send signal over fd(?)

(OSI model vs reality)

Won't cover: (kernel) queues, RT signals, ipfilter subsystem; also TIPC, inotify

* don't be afraid of code
- Python TCP socket server
- C TCP server
- Python UDP socket server

* powerful software uses kernel/hardware knowledge to accomplish magic
- Redis
- Apache
- Varnish vs Squid(?)
- Docker vs LXC + Namespaces + Aufs; layers are *different*
- ? uWSGI, unicorn/gunicorn

* Netflix diagram



* sendmsg()
# find . -name '*.c' | xargs egrep -q sendmsg | egrep -v zmq
- Redis: no
- Apache: ?
	http://httpd.apache.org/docs/current/mod/mod_proxy_fdpass.html
- Nginx: yes
	ngx_channel.c:ngx_write_channel

- Unicorn/Gunicorn:
- Uwsgi: yes
- Varnish: no?
- also
	https://github.com/slideinc/sendmsg -- for Python



