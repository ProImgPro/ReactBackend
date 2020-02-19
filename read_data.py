import sqlite3
import pymongo
from flask import Resource, Api
from flask_restful import

myclient = pymongo.MongoClient("mongodb://bootai:1234567aA%40@27.72.147.222:27017/erp?authSource=admin")
mytable = myclient['test2m']
mycol = mytable['test']


class Data_db(Resource):



if __name__ == '__main__':
    get_data()