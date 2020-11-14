import os

from flask import Flask, make_response
from flask_script import Manager

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

@app.route('/')
def read_info():

    with open(os.path.join(APP_STATIC, 'message.txt'), encoding='utf-8') as f:
        resp = f.read()
        f.close()
    return str(resp)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host='::', port=1089)

