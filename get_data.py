from flask import Flask, jsonify
import pymongo
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource
from marshmallow import fields
from app.utils import parse_req

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
        find_data = list(mycol.find({}, {'_id': 0 }))
        return jsonify(find_data)

    def post(self):
        param = {
            'my_answer': fields.String()
        }
        try:
            json_data = parse_req(param)
            my_answer = json_data.get('my_answer', None)
        except:
            return jsonify("Getting error wrong !")
        try:
            list_answer = list(mycol.find_many({}, {'id': 1, 'answer': 1}))
            print(list_answer)
        except Exception as e:
            return {e}



api.add_resource(Get_Data_MG, '/get_data')

if __name__ == '__main__':
    app.run(port=23486, debug=True)



