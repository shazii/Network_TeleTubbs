# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:09:39 2018

@author: Shameena
"""

from flask import Flask, redirect, url_for, request, json, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Tele Tubbs API<br><br><a href="/login">PLEASE LOGIN<a>'

if __name__ == "__main__":
    app.run(debug=True)
