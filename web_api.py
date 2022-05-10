import json
import pymongo
from flask import Flask, request
from flask_cors import CORS

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['new_db']['students']

app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/')
def app_home():
    return 'Hello'


@app.route('/find_all')
def app_find_all():
    myquery = {}
    myfilter = {'_id': 0}
    result = mydb.find(myquery, myfilter)
    return json.dumps(list(result))


@app.route('/find', methods=['GET'])
def app_find():
    name = request.args.get('name')
    myquery = {'name': name}
    myfilter = {'_id': 0}
    result = mydb.find(myquery, myfilter)
    return json.dumps(list(result))


@app.route('/delete', methods=['GET'])
def app_delete():
    name = request.args.get('name')
    myquery = {'name': name}
    result = mydb.delete_many(myquery)
    deleted = result.deleted_count
    return json.dumps({'deleted': bool(deleted)})


@app.route('/update', methods=['GET'])
def app_update():
    data_str = request.args.get('data')
    data_dict = json.loads(data_str)
    name = data_dict['name']
    myquery = {'name': name}
    count = len(list(mydb.find(myquery)))
    if count == 0:
        result = mydb.insert_one(data_dict)
        inserted_id = str(result.inserted_id)
        return json.dumps({'insert': inserted_id})
    else:
        newvalues = {'$set': data_dict}
        result = mydb.update_one(myquery, newvalues)
        modified_count = result.modified_count
        return json.dumps({'update': bool(modified_count)})


app.run('0.0.0.0', port=5000)
