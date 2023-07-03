from flask import Flask

app = Flask(__name__)


@app.route('/index/<user>', methods=['GET'])
def hello_world(user):
    # aint = 1
    # astr = '1'
    # # aadd = aint + astr
    return 'hello %s' % user


app.run(debug=True)
