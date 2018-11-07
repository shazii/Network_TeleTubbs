from scapy.all import *
from scapy.utils import PcapWriter

def checkPacketLength(packet):
  if IP in packet:
    packetLength = int(packet.sprintf("%IP.len%"))
    #print(packetLength)
    with open("static/quotes.txt", encoding="utf8") as f:
      line = next(f)
    if packetLength > 100 and line.upper() != "OVERLOAD":
      with open('templates/status.txt','w') as f:
        f.write("OVERLOAD")
        print("overload!")
    else:
      if line.upper() != "NORMAL":
        with open('templates/status.txt','w') as f:
          f.write("NORMAL")

while True:
  
  #pkts_list = sniff(filter="tcp port 5000 and IP host 127.0.0.1", timeout=2)
  pkts_list = sniff(prn=checkPacketLength, filter="tcp port 5000 and IP host 127.0.0.1", timeout=2)

  # Overwrites pcap file
  #wrpcap('trace/traffic.pcap', pkts_list)

  # Appends to pcap file
  pktdump = PcapWriter("trace/traffic.pcap", append=True, sync=True)
  pktdump.write(pkts_list)
