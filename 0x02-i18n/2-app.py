#!/usr/bin/env python3

"""Decorator to determine best match for supported languages"""

from flask import Flask, render_template, request
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
    return render_template('2-index.html')

@babel.localeselector
def get_locale():
    """determines best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    