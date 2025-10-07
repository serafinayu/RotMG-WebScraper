import os
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

"""
This module has functions for connecting to the MongoDB and dropping the collection if exists
"""

def get_db():
    load_dotenv()
    MONGO_URI = os.getenv("MONGODB_URI")
    # db_name = os.environ.get('DB_NAME')
    DB_NAME = os.getenv('DB_NAME')

    # Check if environment variables are set
    if not MONGO_URI:
        raise ValueError("The MONGODB_URI environment variable is not set.")
    if not DB_NAME:
        raise ValueError("The DB_NAME environment variable is not set.")

    client = MongoClient(MONGO_URI)
    db = client.get_database(DB_NAME)

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

def insert_items(items_data, subcategory_name, category_name):
    """
    Insert a list of items into the MongoDB items collection
    
    Args:
        items_data (list): List of item dictionaries to insert
        category_name (str): The category name (e.g., 'daggers', 'bows')
    """
    db = get_db()
    collection = db['items']
    
    if not items_data:
        print(f"No items to insert for category: {subcategory_name}")
        return
    
    # Add category and timestamp to each item
    for item in items_data:
        item['category'] = category_name
        item['subcategory'] = subcategory_name
        item['scraped_at'] = datetime.utcnow()
    
    try:
        # Insert many items at once
        result = collection.insert_many(items_data)
        print(f"Successfully inserted {len(result.inserted_ids)} items for category: {category_name}")
        return result.inserted_ids
    except Exception as e:
        print(f"Error inserting items for category {subcategory_name}: {e}")
        return None

def insert_single_item(item_data, category_name):
    """
    Insert a single item into the MongoDB items collection
    
    Args:
        item_data (dict): Item dictionary to insert
        category_name (str): The category name
    """
    db = get_db()
    collection = db['items']
    
    # Add category and timestamp
    item_data['category'] = category_name
    item_data['scraped_at'] = datetime.utcnow()
    
    try:
        result = collection.insert_one(item_data)
        print(f"Successfully inserted item: {item_data.get('name', 'Unknown')} in category: {category_name}")
        return result.inserted_id
    except Exception as e:
        print(f"Error inserting item {item_data.get('name', 'Unknown')}: {e}")
        return None

def get_items_by_category(category_name):
    """
    Retrieve all items from a specific category
    
    Args:
        category_name (str): The category name to filter by
    """
    db = get_db()
    collection = db['items']
    
    try:
        items = list(collection.find({"category": category_name}))
        print(f"Found {len(items)} items in category: {category_name}")
        return items
    except Exception as e:
        print(f"Error retrieving items for category {category_name}: {e}")
        return []

def count_total_items():
    """
    Count total number of items in the database
    """
    db = get_db()
    collection = db['items']
    
    try:
        count = collection.count_documents({})
        print(f"Total items in database: {count}")
        return count
    except Exception as e:
        print(f"Error counting items: {e}")
        return 0