from configparser import ConfigParser
import psycopg2 

# Try to connect to the database, otherwise print an error
try:
    # Create an instance of the parser
    config = ConfigParser()
    # Read the config file
    config.read("config.ini")

    # Store the config details in variables
    database = config.get('DEFAULT', 'database')
    user = config.get('DEFAULT', 'user')
    host = config.get('DEFAULT', 'host')
    password = config.get('DEFAULT', 'password')
    port = config.getint('DEFAULT', 'port')

    # Create a database connection with psycopg2 with the details from the config file
    conn = psycopg2.connect(database=database, 
                            user=user, 
                            host=host,
                            password=password,
                            port=port)
    
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
    print(error)
finally:
    # Close cursor and communication with the database if they exist
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

                        


