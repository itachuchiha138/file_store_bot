import pymongo
from .config import MONGO_URI

client = pymongo.MongoClient(MONGO_URI)
db = client['FileStoreDB']
collection = db['files']

def save_file(file_id, file_name, user_id):
    collection.insert_one({"file_id": file_id, "file_name": file_name, "user_id": user_id})

def get_file(file_id):
    return collection.find_one({"file_id": file_id})
