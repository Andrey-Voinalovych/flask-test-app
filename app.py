from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Worldish!",200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)