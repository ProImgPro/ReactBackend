import json
from flask import jsonify, Response, make_response
from .extensions import parser
from marshmallow import fields, validate as validate_


def send_result(data=None, message="OK", code=200):
    """
    Args:
        data: simple result object like dict, db.Unicode or list
        message: message send to client, default = OK
        code: code default = 200
        version: version of api
    Returns:
        json rendered sting result
    """
    res = {
        "jsonrpc": "2.0",
        "status": True,
        "code": code,
        "message": message,
        "data": data,
    }

    return jsonify(res), 200


def send_error(data=None, message="Error", code=200, version=1):
    """"

    """
    res_error = {
        "jsonrpc": "2.0",
        "status": False,
        "code": code,
        "message": message,
        "data": data
    }
    return jsonify(res_error), code

def send_file(pdf=None, file_name='', code=200):
    """
    Args:
        csv: just pdf file
        code: code default = 200
        file_name: name of file csv
    Returns:
        json rendered sting result
    """
    response = make_response(pdf)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set(
        'Content-disposition', 'attachment', filename=file_name)

    return response, code

def parse_req(argmap):
    """
    Parser request from client
    :param argmap:
    :return:
    """
    return parser.parse(argmap)

