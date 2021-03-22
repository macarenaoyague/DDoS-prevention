import pyshark
import time

DNS = 0
NTP = 0
SNMP = 0
SSDP = 0

server_ip = '10.0.0.5'
threshold = 10

def identify_source_port(source_port):
    if source_port == 53:
        DNS += 1
    elif source_port == 123:
        NTP += 1
    elif source_port == 161:
        SNMP += 1
    elif source_port == 1900:
        SSDP += 1

def check_threshold():
    if DNS > threshold or NTP > threshold or SNMP > threshold or SSDP > threshold:
        print('Server has surpassed the threshold')
        return True
    return False

while True:
    capture = pyshark.LiveCapture(interface='eth0', display_filter='udp')
    capture.sniff(timeout = 5)
    if len(capture) == 0:
        continue
    for packet in capture:
        #print(packet[1].get('dst_host'))
        #print(packet[2].get('srcport'))
        if packet[1].get('dst_host').get_default_value() == server_ip and int(packet[1].get('len').get_default_value()) > threshold:
            identify_source_port(packet[2].get('srcport'))