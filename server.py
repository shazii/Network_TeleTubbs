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

"""
@app.route('/signup', methods = ['POST'])
def signup():
    comment = request.form['comment']
    return render_template("index.html", data=comment)

@app.route('/')
def hello_world():
    author = "Tracy"
    name = "Fellow SUTD-ian"
    return render_template('index.html', author=author, name=name)
"""
comments = []

def generateQuotes():
    with open("static/quotes.txt", encoding="utf8") as f:
            line = next(f)
            for num, aline in enumerate(f,2):
                if random.randrange(num):
                    if line.startswith('--'):
                        line = line[3:]
                    elif line.startswith('\n'):
                        line = next(f)
                    continue
                line = aline
    return line

def generateGraph():
    # Save uploaded file
    #traceFile = request.files['file']
    #filename = secure_filename('{}{}'.format(datetime.now(), traceFile.filename))
    #traceFile.save(filename)  
     
    # Processpcap, creatingpygal chart with packet sizes
    pkt_sizes = []
    pkt_window = []
    cap = pyshark.FileCapture("trace/traffic.pcap", only_summaries=True)
    for packet in cap:
        # Create a point with X=time, Y=bytes
        pkt_sizes.append((float(packet.time), int(packet.length)))
     
    # Create pygal instance
    pkt_size_chart = XY(width=400, height=300, style=LightGreenStyle, explicit_size=True)
    pkt_size_chart.title = 'Packet Sizes'
            
    # Add points to chart andrender html
    pkt_size_chart.add('Size', pkt_sizes)
    chart = pkt_size_chart.render().decode("utf-8")

    return chart

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        chart = generateGraph()
        return render_template('index.html', data=comments, chart=chart)
    if request.method == 'POST':
        n = request.form['quantity']
        chart = generateGraph()
        if n == "":
            return render_template('index.html', data=comments, chart=chart)
        else:
            with open('templates/quantity.txt','w') as f:
                f.write(n)
            for n in range(int(n)):  
                comment = generateQuotes()
                comments.append(comment)
            return render_template("index.html", data=comments, chart=chart)

@app.route('/post', methods = ['POST'])
def hello_world_post():
    return render_template("index.html", data=request.data)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)
