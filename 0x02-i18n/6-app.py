#!/usr/bin/'env python3

"""Uses a user's preferred locale to modify the landing page"""

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
    return render_template('6-index.html')

@babel.localeselector
def get_locale():
    """determines best match with our supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
