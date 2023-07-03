import base64
import random
import time

from flask import Flask, request

app = Flask(__name__)
users = {
    "wanglei": ["123456"]
}


def get_token(uid):
    token = base64.b64decode(':'.join([str(uid), str(random.random()), str(time.time() + 7200)]))
    users[uid].append(token)
    return token


def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request.headers)
    return 'hello'


@app.route('/login', methods=['POST', 'GET'])
def login():
    pass


@app.route('/test', methods=['POST', 'GET'])
def test():
    pass


app.run(debug=True)