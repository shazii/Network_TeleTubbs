# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import random
import os
import pyshark
from datetime import datetime
from pygal import XY
from pygal.style import LightGreenStyle
from werkzeug import secure_filename

app = Flask(__name__)

# a list containing all the current and past messages sent by the client in this session
# initialized as an empty string (no messages) at the start of the session
comments = []


def generateQuotes():
    '''
        Function that returns random lines from a text file containing quotes.
        These lines serve as a placeholder for messages sent by the client and
        to simulate the user experience (for example, what the client will see
        on the webpage when he/she sends a certain number of messages).
    '''
    with open("static/quotes.txt", encoding="utf8") as f:
        line = next(f) # read first line of quotes.txt
        for num, aline in enumerate(f,2): # generate a random number within the number of lines in f
            if random.randrange(num): # check if the current line matches the generated number
                if line.startswith('--'): # line is a name (end of quote)
                    line = line[3:] # only return the name itself (remove '--')
                elif line.startswith('\n'): # empty line (in between quotes)
                    line = next(f) # return the first line of the next quote
                continue # valid line --> exit loop
            line = aline
    return line

def generateGraph():
    '''
        Function that generates the graph which plots the traffic (packet
        size against time). This allows the client to monitor the traffic
        easily, hence improving the user experience while using the webpage.
        For future works, other properties of the packet object can also be
        plotted on the same axes for more detailed analyses and comparisons.
    '''
    # process pcap and create a pygal chart with packet sizes
    pkt_sizes = []
    cap = pyshark.FileCapture("trace/traffic.pcap", only_summaries=True)

    for packet in cap: # for each packet in the pygal chart
        # create a point (X,Y) and add it to the list
        # X: the absolute time (in seconds) between the current packet and the first packet
        # Y: the length (in bytes) of the packet
        pkt_sizes.append((float(packet.time), int(packet.length)))
     
    # create pygal instance
    pkt_size_chart = XY(width=400, height=300, style=LightGreenStyle, explicit_size=True)
    pkt_size_chart.title = 'PACKET SIZES OVER TIME'
    pkt_size_chart.x_title = 'Time (s)'
    pkt_size_chart.y_title = 'Packet Size (bytes)'
            
    # add points to chart and render html
    pkt_size_chart.add('Size', pkt_sizes) # graph legend
    chart = pkt_size_chart.render().decode("utf-8")

    return chart

def readStatus():
    '''
        Function that reads the congestion status (from status.txt) that is
        provided by client.py. It then outputs a string which is displyed on
        the webpage to provide feedback to the client. This allows the client
        to take corrective actions to ease the traffic congestion or for
        future expansions where action is taken by the server to reduce the
        congestion levels.
    '''
    with open("templates/status.txt", encoding="utf8") as f:
        line = next(f) # read status provided by client.py

        # congested traffic (packet size exceeds set threshold)
        if line.upper() == "OVERLOAD":
            return "WARNING! HUGE PACKET DETECTED!"

        # normal traffic (packet size within set threshold)
        else:
            return "NORMAL"

# homepage
@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    '''
        Function that renders the template HTML (index.html) and the
        arguments - data, chart and status - to be displayed on the webpage.
        # data - a list containing all the current and past messages sent by
          the client in this session
        # chart - a string of the HTML script of the chart plotting the
          traffic (packet sizes with time); it is initialized as an empty
          chart at the start of the session (replace the traffic.pcap file
          in the 'trace' folder with the traffic_empty.pcap file before
          starting the session to clear the graph)
        # status - the current congestion status (NORMAL or CONGESTED)
        These arguments are dynamic data that is displayed on the webpage.
    '''
    # view the webpage
    if request.method == 'GET':
        chart = generateGraph()
        return render_template('index.html', data=comments, chart=chart, status=readStatus())

    # submit a POST request by typing an integer (greater than 0) in the input field and pressing the 'Send' button
    if request.method == 'POST': 
        n = request.form['quantity'] # input integer (restricted by form properties to be greater than zero and integer)
        chart = generateGraph()

        if n == "": # no user input
            return render_template('index.html', data=comments, chart=chart, status=readStatus())

        else: # user input (greater than zero and integer)
            # write to quantity.txt to be read by client.py
            # this is used to simulate user traffic by sending one packet for each message sent by the client
            with open('templates/quantity.txt','w') as f:
                f.write(n)
            for n in range(int(n)): # repeat n times
                comment = generateQuotes() # generate a random line from quotes.txt
                comments.append(comment) # add to list of messages
            return render_template("index.html", data=comments, chart=chart, status=readStatus())

# sub-route to simulate user traffic (packets simulating messages are sent here)
@app.route('/post', methods = ['POST'])
def hello_world_post():
    '''
        Placeholder function to receive POST requests from packets simulating
        messages. Clients will not be redirected to this URL.
    '''
    return render_template("index.html", data=request.data)

if __name__ == "__main__":
    #app.run() # execution mode
    app.run(debug=True) # debug mode
