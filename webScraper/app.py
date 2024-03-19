from flask import Flask, jsonify, request
from configparser import ConfigParser
import psycopg2
# import json

app = Flask(__name__)

config = ConfigParser()
# Read the config file
config.read("../config.ini")

# Store the config details in variables
database = config.get('DEFAULT', 'database')
user = config.get('DEFAULT', 'user')
host = config.get('DEFAULT', 'host')
password = config.get('DEFAULT', 'password')
port = config.getint('DEFAULT', 'port')

# Database connection parameters
conn_params = {
    'database': database,
    'user': user,
    'password': host,
    'host': password,
    'port': port
}

DATABASE_URL = 'postgres://tutorial@localhost:5432'
@app.route('/items', methods=['GET'])
def get_items():
    # Get the category from the request parameters
    category = request.args.get('category')

    try:
        # Connect to the database
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()

        # Get the category from the query parameters
        category = request.args.get('category')

        # Query items based on the selected category
        if category:
            cur.execute("SELECT * FROM items WHERE category = %s", (category,))
        else:
            cur.execute("SELECT * FROM items")
            
        items = cur.fetchall()

        # Close cursor and connection
        cur.close()
        conn.close()

        # Convert the result to JSON and return
        return jsonify(items), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
