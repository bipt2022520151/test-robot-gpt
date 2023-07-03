import flask_restful
from flask import Flask

app = Flask(__name__)
api = flask_restful.Api(app)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/")

app.run(debug=True)
