#!/usr/bin/env python3

"""a basic Flask app in 0-app.py. Create a single / route 
and an index.html template that simply outputs “Welcome to Holberton”
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)

def index():
    """index function"""
    return render_template('0-index.html')
