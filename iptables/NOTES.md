iptables -L --line-numbers

http://unix.stackexchange.com/questions/15870/iptables-port-mirroring


sudo iptables -A PREROUTING -t mangle -p tcp -s !127.0.0.1/32 --dport 8001 -j ROUTE --gw 127.0.0.1 --tee
$ sudo iptables -A POSTROUTING -t nat -p tcp -s 127.0.0.1/32 --dport 8001 -j DNAT --to 127.0.0.1:8002

sudo iptables -A INPUT -p TCP --dport 80 -j ULOG --ulog-nlgroup 2
https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html#ULOGTARGET
"deprecated, use NFLOG instead"


sudo `which python` ./pmonitor.py 
https://www.kernel.org/doc/Documentation/accounting/taskstats.txt

{'reserved': 0, 'cmd': 2, 'header': {'pid': 0, 'length': 364, 'flags': 0, 'error': None, 'type': 24, 'sequence_number': 0}, 'version': 1, 'attrs': [['TASKSTATS_TYPE_AGGR_PID', {'attrs': [['TASKSTATS_TYPE_PID', 8949], ['TASKSTATS_TYPE_STATS', {'read_syscalls': 0, 'ac_flag': 0, 'version': 8, 'ac_stimescaled': 0, 'cpu_run_real_total': 0, 'cpu_count': 2, 'ac_utimescaled': 0, 'write_syscalls': 0, 'ac_uid': 123, 'read_bytes': 0, 'hiwater_vm': 4420, 'cpu_scaled_run_real_total': 0, 'cancelled_write_bytes': 0, 'ac_comm': 'df', 'write_char': 0, 'blkio_count': 0, 'swapin_count': 0, 'ac_majflt': 0, 'ac_utime': 0, 'ac_sched': 0, 'ac_ppid': 8948, 'read_char': 3072, 'cpu_delay_total': 2552, 'nvcsw': 0, 'ac_stime': 0, 'coremem': 0, 'virtmem': 0, 'ac_btime': 1400982656, 'ac_exitcode': 0, 'write_bytes': 0, 'ac_etime': 669, 'blkio_delay_total': 0, 'ac_pid': 8949, 'nivcsw': 1, '__pad': 0, 'swapin_delay_total': 0, 'cpu_run_virtual_total': 123144, 'ac_gid': 133, 'ac_minflt': 282, 'ac_nice': 0, 'hiwater_rss': 804}]]}]]}


http://zindilis.com/docs/man/PF_NETLINK.7.html

NETLINK_INET_DIAG

NETLINK_NFLOG


http://kristrev.github.io/2013/07/26/passive-monitoring-of-sockets-on-linux/

http://linux.die.net/man/8/ss -- ss is used to dump socket statistics. It allows showing information similar to netstat. It can display more TCP and state informations than other tools.


http://man7.org/linux/man-pages/man7/rtnetlink.7.html -- NETLINK_ROUTE

exec-notify, so you can watch your acrobat reader or vim executing "bash -c"
 * commands ;-)
NETLINK_CONNECTOR -- http://users.suse.com/~krahmer/exec-notify.c

ALSO


http://www.linuxjournal.com/article/7356 -- general Netlink, old (2005)

