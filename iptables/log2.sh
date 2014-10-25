#!/bin/bash

sudo iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW -j LOG --log-prefix BEER --log-level 7

# May 24 16:28:43 palabras kernel: [ 1126.702792] BEERIN=lo OUT=
# MAC=00:00:00:00:00:00:00:00:00:00:00:00:08:00 SRC=127.0.0.1
# DST=127.0.0.1 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=47075 DF PROTO=TCP
# SPT=37275 DPT=80 WINDOW=43690 RES=0x00 SYN URGP=0
