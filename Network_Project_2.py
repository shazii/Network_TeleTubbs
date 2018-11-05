# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
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

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', data=comments)
    if request.method == 'POST':
        comment = request.form['comment']
        if comment.upper() == 'CLEAR' and len(comment) != 0:
            del comments[:]
        else:
            comments.append(comment)
        return render_template("index.html", data=comments)

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
