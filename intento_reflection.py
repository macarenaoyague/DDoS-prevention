import pyshark
import time
from netaddr import IPAddress

server_ip = '10.0.0.5'

while True:
    capture = pyshark.LiveCapture(interface='eth0', display_filter='udp')
    capture.sniff(timeout = 5)
    if len(capture) == 0:
        continue
    for packet in capture:
        #print(packet[1].get('dst_host'))
        ip = IPAddress(packet[1].get('src_host').get_default_value())
        netmask = ip.netmask_bits
        print(netmask)
        print(packet[1].get('dst_host').get_default_value())
        if packet[1].get('dst_host').get_default_value() == server_ip:
            print('a')