# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import random

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

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', data=comments)
    if request.method == 'POST':
        n = request.form['quantity']
        if n == "":
            return render_template('index.html', data=comments)
        else:
            with open('templates/quantity.txt','w') as f:
                f.write(n)
            for n in range(int(n)):  
                comment = generateQuotes()
                comments.append(comment)
            return render_template("index.html", data=comments)

@app.route('/post', methods = ['POST'])
def hello_world_post():
    return render_template("index.html", data=request.data)

if __name__ == "__main__":
    app.run()    

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


@app.route('/mainpage', methods=['GET','POST'])
def mainpage():
  return contact_form

if __name__ == "__main__":
    app.run(debug=True)
"""
