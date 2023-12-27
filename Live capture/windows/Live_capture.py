import pyshark
import pandas as pd
import os



class Live_capture_pyshark_and_parsing:
     def __init__(self):
          
          os.chdir(os.getcwd() + '\\Live capture\\windows')

          self.pcap_name = "Windows.pcap"
          self.live = self.live_capture_pcap('Adapter for loopback traffic capture') 
          self.pyshark_obj = pyshark.FileCapture(f'Windows.pcap')
          
     def live_capture_pcap(self, NIC : str):
          """"
          This function will capture your Network interface controller and will create a PCAP file

          NIC >>> Your Network interface controller
          
          example >>> Adapter for loopback traffic capture
          """

          capture = pyshark.LiveCapture(interface=NIC, output_file=f'{self.pcap_name}')
          print('Capturing the packets from your machine')
          capture.sniff(timeout=5)
          print(f"Pcap file has been created\n{capture}")

          return capture
     
     def layer_ip(self, file):
          """"
          This function will parser your PCAP file, the data that will be collected are: ip address and ip destination

          file >>>  self.pyshark_obj 
          """
          src_dst = []
          source = []
          destination = []
          
          for packet in file:   
               try:
                   source.append(packet.ip.src)
                   destination.append(packet.ip.dst)
               except AttributeError:
                    print(f'No attribute found, adding None as attribute value')
                    source.append(None)
                    destination.append(None)

          source_dict = {'IP source': source}
          dst_dict = {'IP destination': destination}

          src_dst.append(source_dict)
          src_dst.append(dst_dict)
               
          return src_dst


     def protocol(self, file):
          """
          This function will parser your PCAP file, the data that will be collected is: protocols          
          """
          protocol = {}
          protocol_name = []
          
          for packet in file:
               protocol_name.append(packet.transport_layer)

          protocol['Protocol'] = protocol_name

          return protocol
          

     def epoch_time(self, file):
          """
          This function will parser your PCAP file, the data that will be collected is: Time
          """
          time = {}
          list_time = []
          
          for epoch_time in file:
               date_time = epoch_time.frame_info.time[:-3].strip()
               list_time.append(date_time)

          time['Date'] = list_time

          return time



     def main(self):
          """
          This function will put all the outher function together
          """
          pcap = self.pyshark_obj
          ips = self.layer_ip(pcap)
          protocols = self.protocol(pcap)
          epoch = self.epoch_time(pcap)

          all_data = {}

          all_data['ip Source'] = ips[0]['IP source']
          all_data['ip Destination'] = ips[1]['IP destination']
          all_data['Protocol'] = protocols['Protocol']
          all_data['Time'] = epoch['Date']
      
          df = pd.DataFrame(all_data)
          df.to_csv('Windows.csv', index=False)


File = Live_capture_pyshark_and_parsing()
File.main()
