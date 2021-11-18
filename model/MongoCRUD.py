# MongoDB Access and CRUD test
from pymongo import MongoClient

# 1. MongoDB Connection

# 'localhost' == 127.0.0.1 == 내 IP 주소
client = MongoClient('localhost', 27017) # (IP address, port number)
db = client['local']                     # Allocating 'local' DB
collection = db.get_collection('test')   # Allocating 'review' Collection

data = {'name': 'cherry', 'age': 8}
collection.insert_one(data)

# MongoDB > database > collection > document

# CRUD => Create, Read, Update, Delete