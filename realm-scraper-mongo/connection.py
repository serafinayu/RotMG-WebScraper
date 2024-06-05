import os
from pymongo import MongoClient

"""
This module has functions for connecting to the MongoDB and dropping the collection if exists
"""

def get_db():
    mongodb_uri = os.environ.get('MONGODB_URI')
    db_name = os.environ.get('DB_NAME')

    # Check if environment variables are set
    if not mongodb_uri:
        raise ValueError("The MONGODB_URI environment variable is not set.")
    if not db_name:
        raise ValueError("The DB_NAME environment variable is not set.")

    client = MongoClient(mongodb_uri)
    db = client.get_database(db_name)

    return db

def drop_items_collection():
    db = get_db()
    # Specify the collection name
    collection_name = 'items'
    # Check if the collection exists in the database
    if collection_name in db.list_collection_names():
    # Drop the collection
        db[collection_name].drop()
        print(f"Collection '{collection_name}' dropped!")
    else:
        print(f"Collection '{collection_name}' does not exist.")
    return