from scapy.all import *
from scapy.utils import PcapWriter

while True:
  pkts_list = sniff(filter="tcp port 5000 and IP host 127.0.0.1", timeout=5)

  # Overwrites pcap file
  #wrpcap('trace/traffic.pcap', pkts_list)

  # Appends to pcap file
  pktdump = PcapWriter("trace/traffic.pcap", append=True, sync=True)
  pktdump.write(pkts_list)
