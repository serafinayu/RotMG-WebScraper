
from configparser import ConfigParser
import psycopg2 

"""
This module has functions that creates a connection to the database, gets the database url, 
and creates the table in the database
"""

# Function to connect to the database
def connect_to_db():
    """Returns the connection instance with data from the config file"""
    # Create an instance of the parser and read the config file
    config = ConfigParser()
    config.read("./config.ini")

    # Extract the database connection settings
    conn = psycopg2.connect(
        database=config.get('DEFAULT', 'database'), 
        user=config.get('DEFAULT', 'user'), 
        password=config.get('DEFAULT', 'password'), 
        host=config.get('DEFAULT', 'host'), 
        port=config.get('DEFAULT', 'port'))

    return conn

def get_db_url():
    """Returns the database url for making requests to the database"""
    config = ConfigParser()
    config.read("./config.ini")

    user=config.get('DEFAULT', 'user'), 
    password=config.get('DEFAULT', 'password'), 
    port=config.get('DEFAULT', 'port')

    return (f'postgres://{user}:{password}@localhost:{port}')

def create_db():
    """Deletes the table and recreates it"""
    cur = None
    conn = None
    # Try to connect to the database, otherwise print an error
    try:
        # Create a database connection with psycopg2 with the details from the config file
        conn = connect_to_db()
        
        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Delete the table if it exists
        cur.execute("""DROP TABLE IF EXISTS items""")
        # Create the table
        cur.execute("""CREATE TABLE IF NOT EXISTS items(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR (50) UNIQUE NOT NULL,
                    imgUrl VARCHAR (100) NOT NULL,
                    tier VARCHAR (3) NOT NULL,
                    category VARCHAR (10) NOT NULL,
                    subCategory VARCHAR (20), 
                    amount INTEGER NOT NULL); """
                    )
        
        # Make the changes to the database persistent
        conn.commit()
    except Exception as error:
        # Print any errors that occur in the try statement if any
        print("An error occurred:", error)
    finally:
        # Close cursor and communication with the database if they exist
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
