from scapy.all import *

pkts_list = sniff(timeout=20)
wrpcap('trace/traffic.pcap', pkts_list)
