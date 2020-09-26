# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:13:16 2020.

@author: laura
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/landing_iframe.html')
def landing_iframe():
    return render_template('landing_iframe.html')

if __name__ == '__main__':
    app.run()