# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:14:43 2018

@author: Kaleb Keith


This file initializes your application and brings 
together all of the various components.
"""

from flask import Flask

app = Flask(__name__)

from app import routes
