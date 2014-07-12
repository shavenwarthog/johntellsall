# pylint: disable=W0311
from scapy.all import *
import sys
import datetime
import Queue
from threading import Thread

device_dict = {}
not_an_ap = {}

def packet_handler(pkt):
  if not pkt.haslayer(Dot11):
      return
  sig_str = -(256-ord(pkt.notdecoded[-4:-3]))
  ssid = ''
  try:
    mac_addr = pkt.addr2
    ssid = pkt.info
  except Exception as exc:
      # print 'UHOH:',exc, pkt.__dict__
      return
  if (mac_addr in device_dict 
      and ssid != device_dict[mac_addr]):
    output= "DIS MAC:%s RSSI:%s " %(mac_addr,sig_str)
    print output
    device_dict.pop(mac_addr)
    not_an_ap[mac_addr] = ssid
    # self.queue.put(output)
  elif ssid=="" or pkt.info=="Broadcast":
    output= "DIS MAC:%s RSSI:%s " %(mac_addr,sig_str)
    print output
    # self.queue.put(output)
  else:
    pot_mac=not_an_ap.get(mac_addr)
    if pot_mac is None:
      device_dict[mac_addr] = ssid

sniff(iface="mon1", prn=packet_handler)

#       print 'after run'


# currentQueue=Queue.Queue()

# #object setup
# print'Initialising sniffer'
# packet_sniffer_instance=packet_sniffer(currentQueue)
# # packet_sniffer_instance.daemon=True
# packet_sniffer_instance.start()
# time.sleep(12)
# print'Finished initialising sniffer'
# packet_sniffer_instance.join()
# print 'Joined'
# # time.sleep(1)


