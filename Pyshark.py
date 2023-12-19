import pyshark


def layer_ip(file ='./2023-12-15-TA577-Pikabot-infection-traffic.pcap'):
    pyshark_obj = pyshark.FileCapture(file)
    src_dst_proto_proto = {}
    source = []
    destination = []
    protocol = []
    
    for packet in pyshark_obj:   
       try:
            source.append(packet.ip.src)
            destination.append(packet.ip.dst)
            protocol.append(packet.transport_layer)
       
       except: 
            continue
       
    src_dst_proto_proto['Source'] = source
    src_dst_proto_proto['Destination'] = destination
    src_dst_proto_proto['Protocol'] = protocol

    return src_dst_proto_proto
