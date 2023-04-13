from flask import Flask, jsonify
import random
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient()
    db = client["animal_db"]
    return db

@app.route('/')
def ping_server():
#     db.animal_tb.insertMany([
#     {
#         "id": 1,
#         "name": "Lion",
#         "type": "wild"
#     },
#     {
#         "id": 2,
#         "name": "Cow",
#         "type": "domestic"
#     },
#     {
#         "id": 3,
#         "name": "Tiger",
#         "type": "wild"
#     },
# ])
    return "Welcome to the world of animals."


@app.route('/animals', methods=['GET'])
def get_stored_animals():
    db = get_db()
    coll = db['3rd']
    coll.insert_one({
        '_id': random.randint(1, 1000),
        'name': random.choice(['Lion', 'Cow', 'Tiger']),
        'type': random.choice(['wild', 'domestic'])
    })
    animals = coll.find()
    return jsonify([{
        '_id': str(animal['_id']),
        'name': animal['name'],
        'type': animal['type']
    } for animal in animals])
#     {
#         "_id": 2,
#         "name": "Cow",
#         "type": "domestic"
#     },
#     {
#         "_id": 3,
#         "name": "Tiger",
#         "type": "wild"
#     },
# ])
    # animals = coll.find()
    # anml = []
    # for animal in animals:
    #     anml.append(animal)
    # db=""
    # # try:
    # db = get_db()
    # _animals = db.animal_tb.find()
    # animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    # print(animals)
    # anml = 
    # data = list(coll.find())
    # return data
    # except:
    #     pass
    # finally:
    #     if type(db)==MongoClient:
    #         db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
