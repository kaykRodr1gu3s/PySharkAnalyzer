import pyshark
import os
pcap = pyshark.FileCapture(os.getcwd +'http.pcap', debug=True)

pcap[0]
