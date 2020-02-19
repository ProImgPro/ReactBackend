from flask import Flask, jsonify, request
import pymongo
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource
from marshmallow import fields
from webargs.flaskparser import FlaskParser
from bson import ObjectId
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


class Get_Data_MG(Resource):

    def get(self):
        page_size = request.args.get('page_size', '5')
        page_number = request.args.get('page_number', '0')
        skips = int(page_size) * int(page_number)
        find_data = list(mycol.find({}, {'_id': 0, 'id': 1,  'answer': 1}).skip(skips).limit(int(page_size)))
        return jsonify(find_data)

    def post(self):
        param = {
            "id": fields.Number(),
            "questions": fields.String(),
            "a": fields.String(),
            "b": fields.String(),
            "c": fields.String(),
            "d": fields.String(),
            "answer": fields.Number(),
            "description": fields.String()
        }
        try:
            json_data = parse_req(param)
            id = json_data.get('id', None)
            questions = json_data.get('questions', None)
            a = json_data.get('a', None)
            b = json_data.get('b', None)
            c = json_data.get('c', None)
            d = json_data.get('d', None)
            answer = json_data.get('answer', None)
            description = json_data.get('description', None)
        except:
            return jsonify("An error occurred when getting data !")

        query_params = {
            '_id': str(ObjectId()),
            'id': int(id),
            'questions': questions,
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'answer': int(answer),
            'description': description
        }
        try:
            mycol.insert_one(query_params)
            return jsonify("Insert Successfully !")
        except:
            return jsonify("An error occurred when inserting data !")

    def put(self):
        question_id = request.args.get("_id", None)
        query_question = {
            '_id': question_id
        }
        param = {
            "id": fields.Number(),
            "questions": fields.String(),
            "a": fields.String(),
            "b": fields.String(),
            "c": fields.String(),
            "d": fields.String(),
            "answer": fields.Number(),
            "description": fields.String()
        }
        try:
            json_data = parse_req(param)
            id = json_data.get('id', None)
            questions = json_data.get('questions', None)
            a = json_data.get('a', None)
            b = json_data.get('b', None)
            c = json_data.get('c', None)
            d = json_data.get('d', None)
            answer = json_data.get('answer', None)
            description = json_data.get('description', None)
        except:
            return jsonify("An error occurred when getting data !")

        new_params = {'$set': {
            'id': int(id),
            'questions': questions,
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'answer': int(answer),
            'description': description
            }
        }
        try:
            mycol.update(query_question, new_params)
            return jsonify("Update successfully")
        except:
            return jsonify("An error occurred when inserting data")

    def delete(self):
        question_id = request.args.get("_id", None)
        query_id = {
            '_id': question_id
        }
        try:
            mycol.remove(query_id)
            return jsonify("Delete Successfully !")
        except:
            return jsonify("An error occurred when deleting data")


api.add_resource(Get_Data_MG, '/get_data')

if __name__ == '__main__':
    app.run(port=23410, debug=True)



