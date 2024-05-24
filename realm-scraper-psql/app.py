#!/usr/bin/env python3

from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
from connection import connect_to_db, get_db_url

app = Flask(__name__)

DATABASE_URL = get_db_url()

@app.route('/items', methods=['GET'])
def get_items():

    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM items")

        items = cur.fetchall()

        # Close cursor and connection
        cur.close()
        conn.close()

        # Convert the result to JSON and return
        return jsonify(items), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/items/<category>', methods=['GET'])
def get_items_by_category(category):
    try:
        conn = connect_to_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        # cur = conn.cursor()

        # SQL query to select items from the specified category
        cur.execute("SELECT * FROM items WHERE LOWER(category) = %s;", (category,))
        items = cur.fetchall()
        
        return jsonify(items), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            cur.close()
            conn.close()

@app.route('/items/<category>/<subcategory>', methods=['GET'])
def get_items_by_subcategory(category, subcategory):
    try:
        conn = connect_to_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # SQL query to select items from the specified category and subcategory
        cur.execute("SELECT * FROM items WHERE LOWER(category) = %s AND LOWER(subcategory) = %s;", (category, subcategory))
        items = cur.fetchall()
        
        return jsonify(items), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            cur.close()
            conn.close()

@app.route('/items/search/<itemname>', methods=['GET'])
def get_items_by_name(itemname):
    try:
        conn = connect_to_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        # cur = conn.cursor()

        # SQL query to select items with name similar to search input
        query = 'SELECT * FROM items WHERE LOWER(name) LIKE LOWER(%s);'
        likePattern = f'%{itemname}%'
        cur.execute(query, (likePattern,))
        items = cur.fetchall()
        
        return jsonify(items), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == '__main__':
    app.run(port=5000)