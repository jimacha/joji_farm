#!/usr/bin/python3
""" main file with all the routes """
import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def dashboard():

    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
