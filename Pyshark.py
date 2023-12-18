import pyshark
from datetime import datetime
 

def layer_ip(file ='./http.pcap'):
    pyshark_obj = pyshark.FileCapture(file, display_filter='ip')
    src_dst_proto_proto = {}
    source = []
    destination = []
    protocol = []
    
    for packet in pyshark_obj:   
       try:
            source.append(packet.ip.src)
            destination.append(packet.ip.dst)
            protocol.append(packet.ip.proto)
       
       except: 
            continue
       
    src_dst_proto_proto['Source'] = source
    src_dst_proto_proto['Destination'] = destination
    src_dst_proto_proto['Protocol'] = protocol

    print(src_dst_proto_proto)

    return src_dst_proto_proto


layer_ip()
