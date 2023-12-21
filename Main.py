import pyshark
import pandas as pd

class Live_capture_pyshark_and_parsing:
     
     def __init__(self):
          self.pcap_name = "My_pcap.pcap"
          self.pyshark_obj = pyshark.FileCapture(self.live_capture_pcap())
          
     def live_capture_pcap(self):
          capture = pyshark.LiveCapture(interface='enp0s3', output_file=self.pcap_name)
          print('Capturing the packets from your machine')
          capture.sniff(timeout=5)
          print("Pcap file has been created")
          print(capture)

          return capture
     
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
          self.live_capture_pcap()
          pcap = self.pyshark_obj
          ips = self.layer_ip(pcap)
          protocols = self.protocol(pcap)
          epoch = self.epoch_time(pcap)
          all_data = {}

          all_data['ip Source'] = ips[0]['IP source']
          all_data['ip Destination'] = ips[1]['IP destination']
          all_data['Protocol'] = protocols['Protocol']
          all_data['Epoch'] = epoch['Date']
          
          df = pd.DataFrame(all_data)
          df.to_csv(self.pcap_name, index=False)


File = Live_capture_pyshark_and_parsing()
File.main()