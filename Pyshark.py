import pyshark
from datetime import datetime

def pcap_file(file='./http.pcap'):
    pyshark_obj = pyshark.FileCapture(file)
    print(type(pyshark_obj))
    return pyshark_obj
    

pcap_file()