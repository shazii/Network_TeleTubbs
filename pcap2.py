from scapy.all import *
from scapy.utils import PcapWriter

def checkPacketLength(packet):
  '''
      Function to check the size (in bytes) of each packet and compare with
      a predefined threshold (100 bytes). The congestion status is updated
      accordingly based on the following conditions:
        (i)  if packet size > threshold, traffic is congested
        (ii) if packet size <= threshold, traffic is normal
      The status is then written to a text file (status.txt) to be read by
      server.py.
  '''
  if IP in packet:
    packetLength = int(packet.sprintf("%IP.len%"))

    # read current status from status.txt
    with open("templates/status.txt", encoding="utf8") as f:
      line = next(f)

    # condition (i) is satisfied, i.e. packet size > threshold
    # update status TO "OVERLOAD" if current status is not already "OVERLOAD"
    if packetLength > 100 and line.upper() != "OVERLOAD":
      with open('templates/status.txt','w') as f:
        f.write("OVERLOAD")
        print("overload!")

    # condition (ii) is satisfied, i.e. packet size <= threshold
    # update status to "NORMAL" if current status is not already "NORMAL"
    else:
      if line.upper() != "NORMAL":
        with open('templates/status.txt','w') as f:
          f.write("NORMAL")

while True:
  '''
      Infinite while loop that repeatedly monitors the traffic (packet size
      with time) by sniffing packets on the localhost port and appending the
      data to a traffic.pcap file (initially empty). This traffic.pcap file
      is later read by the server.py file and displayed on the webpage as a
      means to monitor the traffic.
      Future works include using a LiveCapture to monitor packets and update
      the webpage instantaneously instead of writing to a file and reading
      from it (can cause synchronization errors and introduce time lags).
  '''
  # sniffs packets on 127.0.0.1:5000 and checks the length of each packet sniffed
  # each instance of sniffing lasts 2 seconds (timeout)
  pkts_list = sniff(prn=checkPacketLength, filter="tcp port 5000 and IP host 127.0.0.1", timeout=2)

  # Method 1: Overwrites pcap file
  # this method was eliminated as it does not track the trend of the packet sizes with time (only displays one Wireshark instance each time)
  #wrpcap('trace/traffic.pcap', pkts_list)

  # Method 2: Appends to pcap file
  # this method was implemented as it tracks the trend of the packet size with time by appending the packet sizes to the same chart (can see previous data and make comparisons)
  pktdump = PcapWriter("trace/traffic.pcap", append=True, sync=True)
  pktdump.write(pkts_list)
