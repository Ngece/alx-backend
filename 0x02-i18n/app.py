#!/usr/bin/env python3

"""Displays current time zone in the default format"""

from flask import Flask, render_template
from flask_babel import Babel
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

"""instatiates the languages available in the app"""
class Config(object):
    """Configures available languages in the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
@app.route('/', methods=['GET'], strict_slashes=False)

def index():
    """index function"""
    return render_template('index.html')

@babel.localeselector
def get_locale():
    """determines best match with our supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """determines best match with our supported timezones"""
    timezone = request.args.get('timezone')
    if timezone in app.config['BABEL_TIMEZONE']:
        return timezone
    return request.accept_languages.best_match(app.config['BABEL_TIMEZONE'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
