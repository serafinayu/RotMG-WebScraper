import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser
import psycopg2 

headers = {
    'User-Agent': 
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
    "Accept": 
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

url = "https://www.realmeye.com"

def storeItems(link, categoryName, subCategory):
    # link = "/wiki/weapons" | for example
    """This function takes the link and item types and """
    imgSrc = ''
    tier = ''
    name = ''
    # Categories: weapons, abilities, armor, rings
    category = categoryName
    # Sub-categories: daggers, spells, heavy armor, health rings
    subCategory = subCategory

    # Get the img url, tier, and name of the item
    response = requests.get(f'{url}{link}', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    tbodies = soup.find_all('tbody')
    for tbody in tbodies:
        trs = tbody.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            count = 0
            for td in tds[:3]:
                if count == 0:
                    img_tag  = td.find('img')
                    if img_tag is not None:
                        imgSrc = img_tag.get('src')
                        name = img_tag.get('title')
                        count += 1
                elif count == 1:
                    b_tag = td.find('b')
                    if b_tag is not None:
                        tier = b_tag.text
                        print("Tier:", tier)
                        count += 1
                    if name is not None:
                        break
                # Some elements don't have the item name in the first as the title of the first element in the row
                # So if there is no name, after the second column, it will move on to the third column
                elif count == 2:
                    a_tag = td.find('a')
                    if a_tag is not None:
                        name = a_tag.text
                        

            insertItem(name, imgSrc, tier, category, subCategory)


def insertItem(name, imgUrl, tier, category, subCategory):

    cur = None
    conn = None

    # Try to connect to the database, otherwise print an error
    try:
        # Create an instance of the parser and read the config file
        config = ConfigParser()
        config.read("../config.ini")

        # Store the config details in variables
        database_host = config.get('DEFAULT', 'database')
        user = config.get('DEFAULT', 'user')
        host = config.get('DEFAULT', 'host')
        password = config.get('DEFAULT', 'password')
        port = config.getint('DEFAULT', 'port')

        # print(database_host, user, host, password, port)
        # Create a database connection with psycopg2 with the details from the config file
        conn = psycopg2.connect(database=database_host, 
                                user=user, 
                                host=host,
                                password=password,
                                port=port)
        
        # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # Use parameterized queries (safer against SQL injection attacks)
        query = """INSERT INTO items (name, imgUrl, tier, category, subCategory, amount)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (name) DO NOTHING
                    """
        values = (name, imgUrl, tier, category, subCategory, 0)
        
        # Make the changes to the database persistent
        cur.execute(query, values)
        conn.commit()

        print(f'{name} was inserted.')

    except Exception as error:
        # Print any errors that occur in the try statement if any
        print(error)

    finally:
        # Close cursor and communication with the database if they exist
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    