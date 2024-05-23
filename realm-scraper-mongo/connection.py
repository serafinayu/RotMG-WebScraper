import os
from dotenv import load_dotenv
from pymongo import MongoClient
"""
This module has functions for connecting to the MongoDB and dropping the collection if exists
"""

def get_db():
    # Load environment variables from .env file
    load_dotenv()
    # Get the MongoDB URI from the environment variables
    uri = os.getenv('MONGODB_URI')
    # Create a new client and connect to the server
    client = MongoClient(uri)
    # db = client.your_database_name
    db = client['ROTMG-Ssnl-Loot']
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