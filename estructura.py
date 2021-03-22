import pyshark

while True:
    capture = pyshark.LiveCapture(interface='eth0')
    capture.sniff(timeout = 5)
    if len(capture) == 0:
        continue
    print(capture)
    print(capture[0])
~