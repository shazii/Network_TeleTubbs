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
        size against number of packets). This allows the client to monitor
        the traffic easily, hence improving the user experience while using
        the webpage.
    '''
    # process pcap and create a pygal chart with packet sizes
    pkt_sizes = []
    pkt_window = []
    cap = pyshark.FileCapture("trace/traffic.pcap", only_summaries=True)

    for packet in cap: # for each packet in the pygal chart
        # create a point (X = time, Y = packet size in bytes) and add it to the list
        pkt_sizes.append((float(packet.time), int(packet.length)))
     
    # Create pygal instance
    pkt_size_chart = XY(width=400, height=300, style=LightGreenStyle, explicit_size=True)
    pkt_size_chart.title = 'PACKET SIZES OVER TIME'
    pkt_size_chart.x_title = 'Time (s)' # absolute time between the current packet and the first packet
    pkt_size_chart.y_title = 'Packet Size (bytes)' # length of the packet in bytes
            
    # Add points to chart and render html
    pkt_size_chart.add('Size', pkt_sizes) # graph legend
    chart = pkt_size_chart.render().decode("utf-8")

    return chart

def readStatus():
    with open("templates/status.txt", encoding="utf8") as f:
        line = next(f)
        if line.upper() == "OVERLOAD":
            return "WARNING! HUGE PACKET DETECTED!"
        else:
            return "NORMAL"

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        chart = generateGraph()
        return render_template('index.html', data=comments, chart=chart, status=readStatus())
    if request.method == 'POST':
        n = request.form['quantity']
        chart = generateGraph()
        if n == "":
            return render_template('index.html', data=comments, chart=chart, status=readStatus())
        else:
            with open('templates/quantity.txt','w') as f:
                f.write(n)
            for n in range(int(n)):  
                comment = generateQuotes()
                comments.append(comment)
            return render_template("index.html", data=comments, chart=chart, status=readStatus())

@app.route('/post', methods = ['POST'])
def hello_world_post():
    return render_template("index.html", data=request.data)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)
