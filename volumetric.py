import pyshark
import time

start = time.time()
warning_limit = 5
threshold = 3

ACK_warning = 0
SYN_warning = 0
ACK_record = 0
SYN_record = 0
ACK = 0
SYN = 0

ICMP_warning = 0
ICMP_record = 0
ICMP = 0

def ACK_check(packet, seconds):
    global ACK_warning
    global ACK_record
    global ACK
    if packet['TCP'].get('flags_ack').get_default_value() == '1':
        ACK += 1
    ACK_rate = float(ACK)/float(seconds)
    if ACK_rate - ACK_record >= threshold:
        ACK_warning += 1
        if ACK_warning >= warning_limit:
           print('Server has surpassed the threshold')
    else:
        ACK_warning = 0
    ACK_record = ACK_rate

def SYN_check(packet, seconds):
    global SYN_warning
    global SYN_record
    global SYN
    if packet['TCP'].get('flags_syn').get_default_value() == '1':
        SYN += 1
    SYN_rate = float(SYN)/float(seconds)
    if SYN_rate - SYN_record >= threshold:
        SYN_warning += 1
        if SYN_warning >= warning_limit:
           print('Server has surpassed the threshold')
    else:
        SYN_warning = 0
    SYN_record = SYN_rate

def TCP_protocol(packet):
    global warning_limit
    global threshold
    end = time.time()
    seconds = end - start
    ACK_check(packet, seconds)
    SYN_check(packet, seconds)

def ICMP_protocol(packet):
    global warning_limit
"volumetric.py" 82L, 2031C                                                                                                                 1,3           Top
    ACK_rate = float(ACK)/float(seconds)
    if ACK_rate - ACK_record >= threshold:
        ACK_warning += 1
        if ACK_warning >= warning_limit:
           print('Server has surpassed the threshold')
    else:
        ACK_warning = 0
    ACK_record = ACK_rate

def SYN_check(packet, seconds):
    global SYN_warning
    global SYN_record
    global SYN
    if packet['TCP'].get('flags_syn').get_default_value() == '1':
        SYN += 1
    SYN_rate = float(SYN)/float(seconds)
    if SYN_rate - SYN_record >= threshold:
        SYN_warning += 1
        if SYN_warning >= warning_limit:
           print('Server has surpassed the threshold')
    else:
        SYN_warning = 0
    SYN_record = SYN_rate

def TCP_protocol(packet):
    global warning_limit
    global threshold
    end = time.time()
    seconds = end - start
    ACK_check(packet, seconds)
    SYN_check(packet, seconds)

def ICMP_protocol(packet):
    global warning_limit
    global threshold
    global ICMP
    end = time.time()
    seconds = end - start
    ICMP += 1
    ICMP_rate = float(ICMP)/float(seconds)
    if ICMP_rate - ICMP_record >= threshold:
        ICMP_warning += 1
        if ICMP_warning >= warning_limit:
           print('Server has surpassed the threshold')
    else:
        ICMP_warning = 0

while True:
    capture = pyshark.LiveCapture(interface='eth0')
    capture.sniff(timeout = 5)
    if len(capture) == 0:
        continue
    for packet in capture:
        transport_protocol = packet.highest_layer
        if transport_protocol == 'TCP':
            TCP_protocol(packet)
        elif transport_protocol == 'ICMP':
            ICMP_protocol(packet)