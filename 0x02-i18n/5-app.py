#!/usr/bin/env python3

"""User login system  """

from flask import Flask, g, render_template, request

app = Flask(__name__)

""" Mock user database table"""
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """Get the user dictionary based on the user ID.
    Args:
        user_id (int): The user ID to look up in the users dictionary.
    Returns:
        dict or None: The user dictionary if found, or None if the ID cannot be found.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """Execute this function before all other functions to find and set the logged-in user.

    The user ID is extracted from the URL parameter 'login_as' and used to find the corresponding user.
    The user dictionary is then set as a global variable on flask.g.user.
    """
    user_id = request.args.get("login_as", type=int)
    if user_id is not None:
        g.user = get_user(user_id)
    else:
        g.user = None

def get_locale():
    """Get the preferred locale for the user.

    The order of priority for the locale is:
    1. Locale from URL parameters ('login_as' parameter)
    2. Locale from user settings (if available)
    3. Locale from request header
    4. Default locale

    Returns:
        str: The preferred locale for the user.
    """
    """ 1. Locale from URL parameters"""
    user_locale = request.args.get("locale")
    if user_locale:
        return user_locale

    """ 2. Locale from user settings (if available)"""
    if g.user and g.user.get("locale"):
        return g.user["locale"]

    """ 3. Locale from request header"""
    request_locale = request.headers.get("Accept-Language")
    if request_locale:
        return request_locale.split(",")[0]

    """ 4. Default locale"""
    return "en"

@app.route('/')
def index():
    """Render the index.html template and pass the appropriate message based on user login status."""
    locale = get_locale()
    messages = {
        "en": {
            "logged_in": "You are logged in as %(username)s.",
            "not_logged_in": "You are not logged in."
        },
        "fr": {
            "logged_in": "Vous êtes connecté en tant que %(username)s.",
            "not_logged_in": "Vous n'êtes pas connecté."
        }
    }

    """ Get the appropriate message based on login status and locale"""
    if g.user:
        message = messages.get(locale, messages["en"])["logged_in"] % {"username": g.user["name"]}
    else:
        message = messages.get(locale, messages["en"])["not_logged_in"]

    """ Render the index.html template and pass the message to be displayed"""
    return render_template("5-index.html", message=message)

if __name__ == '__main__':
    app.run()
