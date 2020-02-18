from flask import Flask, jsonify
import pymongo
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource
from marshmallow import fields
from webargs.flaskparser import FlaskParser

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
        find_data = list(mycol.find({}, {'_id': 0 , 'id': 1,  'answer': 1}))
        return jsonify(find_data)

    def post(self):
        param = {
            'as': fields.Number(),
            'id_as': fields.Number()
        }
        try:
            json_data = parse_req(param)
            my_answer = json_data.get('as', None)
            id_as = json_data.get('id_as', None)
        except Exception as e:
            return {e}
        try:
            find_data = list(mycol.find({}, {'_id': 0, 'id': 1, 'answer': 1}))
            if find_data['id'] == id_as and find_data['answer'] == my_answer:
                return jsonify("Right")
            return jsonify("Wrong")
        except Exception as e:
            return {e}

api.add_resource(Get_Data_MG, '/get_data')

if __name__ == '__main__':
    app.run(port=23486, debug=True)



