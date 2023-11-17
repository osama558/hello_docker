from markupsafe import escape
from flask import Flask,render_template,redirect,request
from bs import extract
from db import db

def hello_world():
    data = extract('https://en.wikipedia.org/wiki/Table_(information)')
    #print(data)
    nn = db.read()
    #print(nn)
    return render_template("index.html",data=data ,nn=nn)

def name(name):
    return f"<p>Hello, {escape(name)} </p>"

def post():
    name = request.form['name']
    print(name)
    number = request.form['number']
    print(number)
    db.insert_record(name,number)
    