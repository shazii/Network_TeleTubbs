# 50.012 Networks Project #

*Team Name:* TeleTubbs

*Title of Project:* Chat Server Application

*Team Members:*
* Tracy Yee Enying (1002379)
* Valerene Goh Ze Yi (1002457)
* Sng Xue Le Candace (1002276)
* Rahmathulla Shameena Nilofar (1002532)

*Features:*
* Send and receive messages
* Monitor traffic and detect congestion
* Feedback on congestion control

## Instructions to how to run TeleTubbs Chat Server Application ##

1. Please install the following libraries: 
* flask
* pyshark
* pygal
* scapy
* requests

2. Using Python 3:
  1. Run server.py
  2. Run client.py
  3. Run pcap2.py
  4. Open "http://127.0.0.1:5000" localhost on your webserver (preferably Chrome). Enter the desired number of packets to be sent (any integer above 0) in the input field at the bottom of the "Client" box.
  5. You will then be able to view the traffic, i.e. the size of the packets sent over time (refer to the "Traffic" box for the graph), based on the packets captured using Wireshark.
  6. In the "Status" box, the current status shows whether the traffic is normal or congested (huge packet detected) as user feedback.

### Beta version of our chat server application: ###

#### When you first launch the chat server application: ####

![picture alt](https://github.com/shazii/Network_TeleTubbs/blob/master/screenshots/Launch%20Webpage.png)


#### Normal traffic: ####

![picture alt](https://github.com/shazii/Network_TeleTubbs/blob/master/screenshots/Normal%20Traffic.png)


#### Congested traffic: ####

![picture alt](https://github.com/shazii/Network_TeleTubbs/blob/master/screenshots/Congested%20Traffic.png)


Note: The graph and the status are only fetched at time of GET/POST requests. They will be updated real-time in the backend but the updated figures will not be displayed unless the page is refreshed (send another request).

### References: ###
https://www.w3schools.com/cssref/pr_grid-column.asp
https://stackoverflow.com/questions/10552067/get-packet-size-in-scapy-python
https://thepacketgeek.com/graphing-packet-details-with-pyshark-pygal-and-flask/
https://stackoverflow.com/questions/10552067/get-packet-size-in-scapy-python
https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
https://stackoverflow.com/questions/7574092/python-scapy-wrpcap-how-do-you-append-packets-to-a-pcap-file
https://gist.github.com/erickedji/68802
https://www.youtube.com/watch?v=Q9sqfPVadDY
