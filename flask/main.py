from flask import Flask
from flask_restful import Resource, Api, reqparse

host = '0.0.0.0'
port = 5600

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("key1", type=str, location="args")  # 新增来源
        self.parser.add_argument("key2", type=str, location="args")

    def get(self):
        data = self.parser.parse_args()
        value1 = data.get("key1")
        value2 = data.get("key2")
        return {'hello': 'world', value1: value2}


api.add_resource(HelloWorld, '/query')

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
