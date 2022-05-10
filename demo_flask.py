from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/')
def app_home():
    return 'Hello'


@app.route('/hello', methods=['GET'])
def app_hello():
    name = request.args.get('name')
    return f'Hello {name}!'


app.run('0.0.0.0', port=5000)
