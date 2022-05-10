import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["new_db"]["students"]

print('find_all:')
myquery = {}
myfilter = {'_id': 0}
result = mydb.find(myquery, myfilter)
for i in result:
    print(i)
print()

print('update:')
data_str = '{"name":"test","score":60,"exam":[{"score":60,"type":"test"}]}'
data_dict = json.loads(data_str)
name = data_dict['name']
myquery = {'name': name}
count = len(list(mydb.find(myquery)))
if count == 0:
    result = mydb.insert_one(data_dict)
    inserted_id = str(result.inserted_id)
    print({'insert': inserted_id})
else:
    newvalues = {'$set': data_dict}
    result = mydb.update_one(myquery, newvalues)
    modified_count = result.modified_count
    print({'update': bool(modified_count)})
print()

print('find_name:')
name = 'test'
myquery = {'name': name}
myfilter = {'_id': 0}
result = mydb.find(myquery, myfilter)
for i in result:
    print(i)
print()

print('delete:')
name = 'test'
myquery = {'name': name}
result = mydb.delete_many(myquery)
deleted = result.deleted_count
print({'deleted': bool(deleted)})
print()
