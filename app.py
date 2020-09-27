# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:13:16 2020.

@author: laura
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home(iframe="landing_iframe"):
    return render_template("home.html", iframe = iframe)

@app.route('/previews/landing_iframe.html')
def landing_iframe():
    return render_template('/previews/landing_iframe.html')

@app.route("/previews/cards.html")
def preview_cards():
    return render_template("/previews/cards.html")

@app.route("/previews/characters.html")
def preview_characters():
    return render_template("/previews/characters.html")

@app.route("/previews/text.html")
def preview_text():
    return render_template("/previews/text.html")

@app.route("/previews/instructions.html")
def instructions():
    return render_template("/previews/instructions.html")

if __name__ == "__main__":
    app.run()