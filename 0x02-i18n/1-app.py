#!/usr/bin/env python3

"""Instatiates a babel object to configure available languages in the app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

"""instatiates the languages available in the app"""
class Config(object):
    """Configures available languages in the app"""
    LANGUAGES = ['en', 'fr']

app.config.from_object(Config)
@app.route('/', methods=['GET'], strict_slashes=False)

def index():
    """index function"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
