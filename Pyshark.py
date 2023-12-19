import pyshark
from datetime import datetime
import json
import pandas as pd


class FileCapture_pyshark:
     def __init__(self):
          self.pyshark_obj = pyshark.FileCapture('./2023-12-15-TA577-Pikabot-infection-traffic.pcap')

               
     def layer_ip(self, file):
          src_dst = []
          source = []
          destination = []
          
          for packet in file:   
               try:
                    source.append(packet.ip.src)
                    destination.append(packet.ip.dst)
               
               except: 
                    continue
          source_dict = {'IP source': source}
          dst_dict = {'IP destination': destination}

          src_dst.append(source_dict)
          src_dst.append(dst_dict)
               
          return src_dst


     def protocol(self, file):
          protocol = {}
          protocol_name = []
          
          for packet in file:
               
               protocol_name.append(packet.transport_layer)

          protocol['Protocol'] = protocol_name

          return protocol
          

     def epoch_time(self, file):
          time = {}
          list_time = []
          
          for epoch_time in file:
               date_time = epoch_time.frame_info.time[:-3].strip()
               list_time.append(date_time)
          time['Date'] = list_time

          return time



     def main(self):
          a = self.pyshark_obj
          ips = self.layer_ip(a)
          protocols = self.protocol(a)
          epoch = self.epoch_time(a)

          all_data = {}

          all_data['ip Source'] = ips[0]['IP source']
          all_data['ip Destination'] = ips[1]['IP destination']
          all_data['Protocol'] = protocols['Protocol']
          all_data['Epoch'] = epoch['Date']
          

          df = pd.DataFrame(all_data)
          df.to_csv('Pcap_content.csv', index=False)





a = FileCapture_pyshark()
# ip_layer = a.layer_ip(a.pyshark_obj) 
# print(ip_layer[1])
a.main()