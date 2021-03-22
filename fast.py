import pyshark
import time

n = 2

while True:
    capture = pyshark.LiveCapture(interface='eth0')
    capture.sniff(timeout = 5)
    if len(capture) == 0:
        continue
    traffic_rate = len(capture)/5
    if traffic_rate > n:
        print('Deep screening')