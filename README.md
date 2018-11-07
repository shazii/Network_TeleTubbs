#Network Project Tele Tubbs#

##Project Title: Chat server application with some additional features, eg. detect congestion and provide feedback.##

###Instructions to run TeleTubbs Chat Server Application###

Please install the following libraries: 
*flask
*pyshark
*pygal
*scapy
*requests

Using python 3: 
1. Run server.py
2. Run client.py
3. Run pcap2.py
4. Open http://127.0.0.1:5000 localhost webserver. Enter the desired number of packets to be sent.
5. You will then be able to view the traffic flow of the packet size over time for the number of packets sent, based on the packet capture.

###Beta version of our chat server application:###

When you first launch the chat server application: ![picture alt](https://github.com/shazii/Network_TeleTubbs/blob/master/screenshots/Launch%20Webpage.png)

Normal traffic: ![picture alt](https://github.com/shazii/Network_TeleTubbs/blob/master/screenshots/Normal%20Traffic.png)

Congested traffic: ![picture alt](https://github.com/shazii/Network_TeleTubbs/blob/master/screenshots/Congested%20Traffic.png)


###References:###
https://www.w3schools.com/cssref/pr_grid-column.asp
https://stackoverflow.com/questions/10552067/get-packet-size-in-scapy-python
https://thepacketgeek.com/graphing-packet-details-with-pyshark-pygal-and-flask/
https://stackoverflow.com/questions/10552067/get-packet-size-in-scapy-python
https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
https://stackoverflow.com/questions/7574092/python-scapy-wrpcap-how-do-you-append-packets-to-a-pcap-file
https://gist.github.com/erickedji/68802
https://www.youtube.com/watch?v=Q9sqfPVadDY
