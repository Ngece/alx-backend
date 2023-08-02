0-app.py                Contains a basic Flask app with a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).



1-app.py                Instantiates a Babel object in the app and stores it in a module-level variable named babel.



2-app.py                 Contains a get_locale function with the babel.localeselector decorator. Uses request.accept_languages to determine the best match with the supported languages.



3-app.py                 Contains 
babel.cfg                A babel config file containing:
    [python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_