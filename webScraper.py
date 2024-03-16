import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
    "Accept": 
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

# item-category-types
itemCategory = ['weapons', 'abilities', 'armor', 'rings', 'etc']

# item-types
weaponTypes = []
abilities = []
armor = []

# possible links
mainLinks = ['weapons', 'ability-items', 'armor', 'rings']
weaponLinks = []
abilityLinks = []
armorLinks = []
ringLinks = []

def getLinks(links):

    mainLinks = links

    def getWeaponLinks(link):
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
                
                # Filter out all the links that have img children
                for a_tag in a_tags:
                    # Check if the <a> tag has no other child elements
                    if len(a_tag.contents) == 1 and not a_tag.find_all():
                        filtered_a_tags.append(a_tag)

                # Extract href and text attributes and store them in arrays
                for a_tag in filtered_a_tags:
                    weaponTypes.append(a_tag.text)
                    weaponLinks.append(a_tag.get('href'))
          
        
    
    def getAbilityLinks(link):
        response = requests.get(f'https://www.realmeye.com/wiki/{link}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        wiki_page_div = soup.find('div', class_='wiki-page')

        if wiki_page_div:
            tbody = wiki_page_div.find('tbody')
            if tbody:
                a_tags = tbody.find_all('a')

                for a_tag in a_tags:
                    abilities.append(a_tag.text)
                    abilityLinks.append(a_tag.get('href'))

    def getArmorLinks(link):
        response = requests.get(f'https://www.realmeye.com/wiki/{link}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        wiki_page_div = soup.find('div', class_='wiki-page')

        if wiki_page_div:
            ul = wiki_page_div.find('ul')

            if ul:
                # Find all <a> tags with both href attribute and text content
                a_tags = ul.find_all('a', href=True, string=True)

                filtered_a_tags = []
                
                # Filter out all the links that have img children
                for a_tag in a_tags:
                    # Check if the <a> tag has no other child elements
                    if len(a_tag.contents) == 1 and not a_tag.find_all():
                        filtered_a_tags.append(a_tag)

                # Extract href and text attributes and store them in arrays
                for a_tag in filtered_a_tags:
                    armor.append(a_tag.text)
                    armorLinks.append(a_tag.get('href'))

    def getRingLinks(link):
        pass

    for link in mainLinks:
        if link == 'weapons':
            getWeaponLinks(link)
        elif link == 'ability-items':
            getAbilityLinks(link)
        elif link == 'armor':
            getArmorLinks(link)
        elif link == 'rings':
            getRingLinks(link)


getLinks(mainLinks)
print(weaponTypes)
print(weaponLinks)
print(abilities)
print(abilityLinks)
print(armor)
print(armorLinks)