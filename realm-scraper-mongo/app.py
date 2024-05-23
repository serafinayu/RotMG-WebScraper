#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_cors import CORS
from bson.json_util import dumps
from connection import get_db

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

db = get_db()

"""Returns all items"""
@app.route('/items', methods=['GET'])
def get_items():
    try:
        items = db.items.find()
        return dumps(items), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

"""Returns all items of the category specified"""
@app.route('/items/<category>', methods=['GET'])
def get_items_by_category(category):
    try:
        items = db.items.find({'category': category.lower()})
        return dumps(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

"""Returns all items of the category and subcategory specified"""
@app.route('/items/<category>/<subcategory>', methods=['GET'])
def get_items_by_subcategory(category, subcategory):
    try:
        items = db.items.find({'category': category.lower(), 'subcategory': subcategory.lower()})
        return dumps(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

"""Returns items with similar names to the input"""
@app.route('/items/search/<itemname>', methods=['GET'])
def get_items_by_name(itemname):
    try:
        items = db.items.find({'name': {'$regex': itemname, '$options': 'i'}})
        return dumps(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

"""Returns all categories"""
@app.route('/items/categories', methods=['GET'])
def get_categories():
    try:
        categories = db.items.distinct('category')
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

"""Returns the subcategories of the input category"""
@app.route('/items/<category>/subcategories', methods=['GET'])
def get_subcategories(category):
    try:
        subcategories = db.items.distinct('subcategory', {'category': category.lower()})
        return jsonify(subcategories), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
