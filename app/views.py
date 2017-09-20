# views.py

from flask import render_template

from app import app

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/login')
def signin():
    return render_template("signin.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")