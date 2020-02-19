from flask import Flask, jsonify, request
import pymongo
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource
from marshmallow import fields
from webargs.flaskparser import FlaskParser
from app.utils import send_result
parser = FlaskParser()



def parse_req(argmap):
    """

    :param argmap:
    :return:
    """
    return parser.parse(argmap)


app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["MONGO_URI"] = "mongodb://bootai:1234567aA%40@27.72.147.222:27017/erp?authSource=admin"

jwt = JWTManager(app)

app.secret_key = 'Yep'


api = Api(app)

myclient = pymongo.MongoClient("mongodb://bootai:1234567aA%40@27.72.147.222:27017/erp?authSource=admin")
mytable = myclient['test2m']
mycol = mytable['test']


class Check_Answer(Resource):
    def post(self):
        params = {
            'answer': fields.List(fields.Dict())
        }
        try:
            json_data = parse_req(params)
            data = json_data.get('answer', None)
        except Exception as e:
            return {e}

        try:
            list_data = []
            find_data = list(mycol.find({}, {'_id': 0, 'id': 1, 'answer': 1}))
            for item in find_data:
                a = False
                for dic in data:
                    if item['id'] == dic['id']:
                        if item['answer'] == dic['answer']:
                            a = True

                list_data.append({
                    'id': item['id'],
                    'answer': a
                })
        except Exception as e:
            return {e}
        return jsonify(list_data)


class Get_By_Id_And_Question(Resource):
    def get(self):
        question_number = request.args.get('question_number', None)
        question_id = request.args.get('question_id', None)
        find_id = mycol.find({}, {'_id': question_id})

        if not find_id:
            return jsonify("Can't be found data")

        page_size = request.args.get('page_size', '5')
        page_number = request.args.net('page_number', 0)
        skips = int(page_number) * int(page_size)

        query = {'$and': [{'_id': question_id}, {'id': question_number}]}
        list_question = list(mycol.find(query).skip(skips).limit(int(page_size)))
        totals = list_question.count()
        send_data = {
            'totals': totals,
            'list_question': list_question
        }
        return jsonify(list(send_data))


