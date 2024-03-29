import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
    "Accept": 
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

def getLinks(link):
    """This function gets and stores all the links needed to pull item data"""

    def getWeaponLinks(link):
        """This function gets all weapon links and stores the names of the weapon types"""

        weapons = {}

        response = requests.get(f'https://www.realmeye.com/wiki/{link}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # For some reason doing soup.find('div.wiki-page') DOESN'T WORK WITH BEAUTIFUL SOUP thus the following:
        wiki_page_div = soup.find('div', class_='wiki-page')

        if wiki_page_div:
            ul = wiki_page_div.find('ul')

            if ul:
                # Find all <a> tags with both href attribute and text content
                a_tags = ul.find_all('a', href=True, string=True)

                filtered_a_tags = []
                
                # Filter out all the links that have img children (ignores links to classes)
                for a_tag in a_tags:
                    # Check if the <a> tag has no other child elements
                    if len(a_tag.contents) == 1 and not a_tag.find_all():
                        filtered_a_tags.append(a_tag)

                # Extract href and text attributes and store them in arrays
                for a_tag in filtered_a_tags:
                    weapons = {**weapons, a_tag.text: a_tag.get('href')}
        
        return weapons
        
    
    def getAbilityLinks(link):
        """This function gets all ability links and stores the names of the ability types"""

        abilities = {}

        response = requests.get(f'https://www.realmeye.com/wiki/{link}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        wiki_page_div = soup.find('div', class_='wiki-page')

        if wiki_page_div:
            tbody = wiki_page_div.find('tbody')
            if tbody:
                a_tags = tbody.find_all('a')

                for a_tag in a_tags:
                    abilities = {**abilities, a_tag.text: a_tag.get('href')}
        
        return abilities

    def getArmorLinks(link):
        """This function gets all armor links and stores the names of the armor types"""
        
        armor = {}
        response = requests.get(f'https://www.realmeye.com/wiki/{link}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        wiki_page_div = soup.find('div', class_='wiki-page')

        if wiki_page_div:
            ul = wiki_page_div.find('ul')

            if ul:
                # Find all <a> tags with both href attribute and text content
                a_tags = ul.find_all('a', href=True, string=True)

                filtered_a_tags = []
                
                # Filter out all the links that have img children (ignores links to classes)
                for a_tag in a_tags:
                    # Check if the <a> tag has no other child elements
                    if len(a_tag.contents) == 1 and not a_tag.find_all():
                        filtered_a_tags.append(a_tag)

                # Extract href and text attributes and store them in arrays
                for a_tag in filtered_a_tags:
                    armor = {**armor, a_tag.text: a_tag.get('href')}
        
        return armor

    def getRingLinks(link):
        """This function gets all ring links and stores the names of the ring types"""

        rings = {}

        response = requests.get(f'https://www.realmeye.com/wiki/{link}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        wiki_page_div = soup.find('div', class_='wiki-page')

        if wiki_page_div:
            tbody = wiki_page_div.find('tbody')
            if tbody:
                # Find all <a> tags with both href attribute and text content
                a_tags = tbody.find_all('a', href=True, string=True)

                filtered_a_tags = []
                
                # Filter out all the links that have img children (ignores links to classes)
                for a_tag in a_tags:
                    # Check if the <a> tag has no other child elements
                    if len(a_tag.contents) == 1 and not a_tag.find_all():
                        filtered_a_tags.append(a_tag)

                # Extract href and text attributes and store them in arrays
                for a_tag in filtered_a_tags:
                    rings = {**rings, a_tag.text: a_tag.get('href')}
        
        return rings
    
    if link == 'weapons':
        return getWeaponLinks(link)
    elif link == 'ability-items':
        return getAbilityLinks(link)
    elif link == 'armor':
        return getArmorLinks(link)
    elif link == 'rings':
        return getRingLinks(link)
    else:
        return {}