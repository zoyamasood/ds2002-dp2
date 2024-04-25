#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.rpk4wp
# specify a collection
collection = db.dp2

#Listing Directory Contents 
path = "." 
for (root, dirs, file) in os.walk(path): 
    for f in file: 
        file_path = os.path.join(root, f)
        print("processing file:", file_path)

#Importing files    
        try: 
            with open(file_path) as file:
                file_data = json.load(file)
                print("file data:", file_path)
            if isinstance(file_data, list): 
                collection.insert_many(file_data)
            else: 
                collection.insert_one(file_data)
            print("records imported", file_path)
        except Exception as e: 
            print("records corrupted", file_path + ":", {e})


