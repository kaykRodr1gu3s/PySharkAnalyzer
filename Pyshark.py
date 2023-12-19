import pyshark
from datetime import datetime

def layer_ip(file ='./2023-12-15-TA577-Pikabot-infection-traffic.pcap'):
    pyshark_obj = pyshark.FileCapture(file)
    src_dst = {}
    source = []
    destination = []
    
    
    for packet in pyshark_obj:   
       try:
            source.append(packet.ip.src)
            destination.append(packet.ip.dst)
       
       except: 
            continue
       
    src_dst['Source'] = source
    src_dst['Destination'] = destination

    return src_dst


def protocol(file = './2023-12-15-TA577-Pikabot-infection-traffic.pcap'):
     protocol = {}
     protocol_name = []
     pyshark_obj = pyshark.FileCapture(file)

     for packet in pyshark_obj:
          
          protocol_name.append(packet.transport_layer)

     protocol['Protocol'] = protocol_name

     return protocol
       

def epoch_time(file = './2023-12-15-TA577-Pikabot-infection-traffic.pcap'):
     pyshark_obj = pyshark.FileCapture(file)
     for c in pyshark_obj:
         epoch = float(c.frame_info.time_epoch)
         date_time = datetime.fromtimestamp(epoch)
         print(date_time)
         input()

