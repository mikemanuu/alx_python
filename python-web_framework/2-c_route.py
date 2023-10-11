#!/usr/bin/python3
""" starts a Flask web application and displays 'Hello HBNB', 'HBNB' and 'C' """
from flask import Flask

app = Flask(__name__)

# this route is called by default when you run it


@app.route('/', strict_slashes=False)
def hello_hbnb():
    # displays message fto the user
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # display HBNB message to the user
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_custom_text(text):
    # display C with text to the user
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
