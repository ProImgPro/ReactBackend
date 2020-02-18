# coding=utf-8
# -*- coding: utf-8 -*-
import os
import logging
import traceback
from time import strftime
from flask import Flask, request
from app.extensions import db, app_log_handler
from app.settings import ProdConfig
from flask_cors import CORS
from app import api


def create_app(config_object=ProdConfig):
    """
    Init App
    :param config_object:
    :param name:
    :return:
    """
    app = Flask(__name__, static_url_path="", static_folder="./template", template_folder="./template")
    app.config.from_object(config_object)
    CORS(app)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """
    Init extension
    :param app:
    :return:
    """
    db.init_app(app)

    @app.teardown_request
    def teardown_request(exception):
        if exception:
            db.session.rollback()
        db.session.remove()

    if os.environ.get('FLASK_DEBUG') != '1':
        # logger
        logger = logging.getLogger('api')
        logger.setLevel(logging.ERROR)
        logger.addHandler(app_log_handler)

        @app.after_request
        def after_request(response):
            # This IF avoids the duplication of registry in the log,
            # since that 500 is already logged via @app.errorhandler.
            if response.status_code != 500:
                ts = strftime('[%Y-%b-%d %H:%M]')
                logger.error('%s %s %s %s %s %s',
                             ts,
                             request.remote_addr,
                             request.method,
                             request.scheme,
                             request.full_path,
                             response.status)
            return response

        @app.errorhandler(Exception)
        def exceptions(e):
            ts = strftime('[%Y-%b-%d %H:%M]')
            tb = traceback.format_exc()
            logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                         ts,
                         request.remote_addr,
                         request.method,
                         request.scheme,
                         request.full_path,
                         tb)
            return "Internal Server Error", 500


def register_blueprints(app):
    """
    Init blueprint for api url
    :param app:
    :return:
    """
    app.register_blueprint(api.questions_data.api, url_prefix='/api/questions')



