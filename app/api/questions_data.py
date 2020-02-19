from flask import Blueprint
from app.utils import send_result, send_error, send_file, parse_req, fields
# from app.model import qa
import sqlite3


api = Blueprint('questions', __name__)


@api.route('', methods=['GET'])
def get_data():
    """
    get data questions
    url: /api/questions
    :return: data questions
    """
    try:
        list_data = []
        conn = sqlite3.connect('./test.db')
        c = conn.execute('SELECT * FROM qa;')
        data = c.fetchall()
        for item in data:
            list_data.append({
                'id': item[0],
                'questions': item[1],
                'a': item[2],
                'b': item[3],
                'c': item[4],
                'd': item[5],
                'description': item[7]
            })
    except Exception as e:
        return send_error(message='DB error')
    finally:
        conn.close()
    return send_result(data=list_data)


@api.route('', methods=['POST'])
def check_answer():
    """
    check answer
    url: /api/questions
    :return: data answer
    """

    params = {
        'answer': fields.List(fields.Dict())
    }
    try:
        json_data = parse_req(params)
        data = json_data.get('answer')
    except Exception as ex:
        return send_error(message='{}'.format(str(ex)), code=442)

    try:
        list_data = []
        conn = sqlite3.connect('./test.db')
        conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
        c = conn.execute('SELECT qa.id, qa.answer FROM qa;')
        list_answer = c.fetchall()
        for item in list_answer:
            a = False
            for dic in data:
                if dic['id'] == item['id']:
                    if dic['value'] == int(item['answer']):
                        a = True
                    break
            list_data.append({
                'id': item['id'],
                'answer': a
            })
    except Exception as e:
        return send_error(message='DB error')
    finally:
        conn.close()
    return send_result(data=list_data)


