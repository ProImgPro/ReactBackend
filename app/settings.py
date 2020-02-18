# -*- coding: utf-8 -*-
import os
os_env = os.environ


class Config(object):
    SECRET_KEY = '3nF3Rn0'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProdConfig(Config):
    """Production configuration."""
    # app config
    ENV = 'prod'
    DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    HOST = '0.0.0.0'
    TEMPLATES_AUTO_RELOAD = False
    # SQL Alchemy config
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////‪C:\\Users\\BootAI\\Downloads\\test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """Development configuration."""
    # app config
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True  # Disable Debug toolbar
    TEMPLATES_AUTO_RELOAD = True
    HOST = '0.0.0.0'
    # SQL Alchemy config
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////‪C:\\Users\\BootAI\\Downloads\\test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
