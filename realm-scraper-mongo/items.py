import requests
from bs4 import BeautifulSoup
import connection

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
    items = []
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
                        
                        count += 1
                    if name is not None:
                        break
                # Some elements don't have the item name in the first as the title of the first element in the row
                # So if there is no name, after the second column, it will move on to the third column
                elif count == 2:
                    a_tag = td.find('a')
                    if a_tag is not None:
                        name = a_tag.text
                
            print("Name:", name, "Tier:", tier)
            item = {
                "name": name,
                "imgUrl": imgSrc,
                "tier": tier,
                "category": category,
                "subcategory": subCategory,
                "amount": 0
            }
            print(item)
            items.append(item)

    return items


def insertItems(items):
    try:
        db = connection.get_db()
        items_collection = db.items
        # Insert the document into the items collection
        items_collection.insert_many(items)
        print("Items have been added to database")

    except Exception as error:
        # Print any errors that occur in the try statement if any
        print(error)
