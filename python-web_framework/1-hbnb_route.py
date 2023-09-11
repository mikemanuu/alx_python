#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask
app = Flask(__name__)

# this route is called by default when you run it


@app.route("/", strict_slashes=False)
def display():
    # displays message for user
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def show_message():
    # display HBNB message for user
    return("HBNB")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
