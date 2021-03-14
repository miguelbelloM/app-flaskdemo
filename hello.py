from flask import Flask

app = Flask(__name__)


@app.route('/l')
def hello():
    return 'Hello World!'
