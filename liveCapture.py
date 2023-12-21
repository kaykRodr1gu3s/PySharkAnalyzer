import pyshark

capture = pyshark.LiveCapture(interface='enp0s3', output_file='aaaaaaaaaaaa.pcap')
capture.sniff(timeout=3)
for c in capture:
    print(c)
    input()