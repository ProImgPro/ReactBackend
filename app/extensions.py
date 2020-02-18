# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""
from webargs.flaskparser import FlaskParser
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

parser = FlaskParser()
app_log_handler = RotatingFileHandler('logs/app.log', maxBytes=1000000, backupCount=30)
db = SQLAlchemy()
