from scapy.all import *

pkts_list = sniff(filter="tcp port 5000 and IP host 127.0.0.1", timeout=20)
wrpcap('trace/traffic.pcap', pkts_list)
