import sqlite3
import pymongo

myclient = pymongo.MongoClient("mongodb://bootai:1234567aA%40@27.72.147.222:27017/erp?authSource=admin")
mytable = myclient['test2m']
mycol = mytable['test']


def get_data():

        conn = sqlite3.connect('./test.db')

        conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
        c = conn.execute('SELECT * FROM qa;')
        data = c.fetchall()
        for item in data:
            print(item)
            mycol.insert(data)


if __name__ == '__main__':
    get_data()