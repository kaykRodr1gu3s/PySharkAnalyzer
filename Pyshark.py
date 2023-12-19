import pyshark
from datetime import datetime
import csv

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
     time = {}
     list_time = []
     pyshark_obj = pyshark.FileCapture(file)
     
     for epoch_time in pyshark_obj:
          date_time = epoch_time.frame_info.time[:-3].strip()
          list_time.append(date_time)
     time['Time'] = list_time

     return time



def main(file_name = './2023-12-15-TA577-Pikabot-infection-traffic.pcap'):









