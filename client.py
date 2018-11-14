import requests

# placeholder URL to send packets (simulate user traffic)
url = 'http://127.0.0.1:5000/post'

while True:
  '''
      Infinite while loop that repeatedly reads the quantity.txt file and
      sends a corresponding number of packets to simulate user traffic.
      The number of packets sent is equal to the number of messages sent by
      the client.
      Note: there are two modes for monitoring the traffic:
        (i)  the packet size with time       --> running client.py is NOT REQUIRED
        (ii) the number of packets with time --> running client.py is REQUIRED
  '''
  n = 0 # number of messages sent by the client (initialized to 0 at the start of the session)
  
  with open("templates/quantity.txt", encoding="utf8") as f:
    n = f.read() # read number from quantity.txt file
    if n != "": # file contains a number (n messages sent)
      n = int(n) # convert the string read from the file to an integer for further processing
    else: # file is empty (no messages sent)
      n = 0 # set number of messages to 0

  # if at least one message was sent, clear the quantity.txt file and send n packets to the placeholder URL
  if n != 0:
    with open('templates/quantity.txt','w'):
      pass # write nothing
  while n > 0: # send n packets (n messages)
    payload = {'quote': "1"}
    r = requests.post(url, json=payload)
    print(r.text)
    print(r.status_code)
    n -= 1

