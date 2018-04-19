# -*- coding: utf-8 -*-
"""
Author: Kaleb Keith
GitHub: https://www.github.com/mynameiskaleb

This is where the routes are defined. It may be 
split into a package of its own (yourapp/views/) 
with related views grouped together into modules.
It is sometimes called routes
"""
from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")
