from scapy.all import sniff, wrpcap
pkts_list = sniff(iface='lo0', timeout=20)
wrpcap('try2.pcap', pkts_list)
