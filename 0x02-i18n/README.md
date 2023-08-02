0-app.py                Contains a basic Flask app with a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).



1-app.py                Instantiates a Babel object in the app and stores it in a module-level variable named babel.



2-app.py                 Contains a get_locale function with the babel.localeselector decorator. Uses request.accept_languages to determine the best match with the supported languages.



3-app.py                 Contains 
    babel.cfg                A babel config file containing:
        [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_
    files translations/[en|fr]/LC_MESSAGES/messages.po must provide the correct value for each message ID for each language. 



4-app.py                 Implements a way to force a particular locale by passing the locale=fr parameter to the app’s URLs.
    detects if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resorts to the previous default behavior.



5-app.py                 Mocks a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.
    Contains a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.
    Contains a before_request function and uses the app.before_request decorator to make it be executed before all other functions. before_request uses get_user to find a user if any, and set it as a global on flask.g.user.



6-app.py                 Changes the get_locale function to use a user’s preferred local if it is supported.
    The order of priority should is:
        Locale from URL parameters
        Locale from user settings
        Locale from request header
        Default locale



7-app.py                 Contains a get_timezone function and use the babel.timezoneselector decorator.
    The is the same as get_locale:
        Find timezone parameter in URL parameters
        Find time zone from user settings
        Default to UTC
    Before returning a URL-provided or user time zone, the time zone is validated. 



app.py                   Display the current time on the home page in the default format based on the inferred time zone.