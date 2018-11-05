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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'username' and request.form['password'] == 'password':
            return redirect(url_for('mainpage'))
    return '''<form action="" method="post">
        <input type="text" placeholder="Username" name="username">
        <input type="password" placeholder="Password" name="password">
        <input type="submit" value="Login">
    </form>'''


@app.route('/mainpage', methods=['GET'])
def mainpage():
    return 'Welcome to Tele Tubbs Main Page'






if __name__ == "__main__":
    app.run(debug=True)
