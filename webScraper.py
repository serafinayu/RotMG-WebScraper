from config_files import create_config
from connection import create_db
from links import getLinks
from items import storeItems

def main():
    # Create the config file
    create_config()
    # Create the table in the database
    create_db()

    # item-category-types
    itemCategory = ['weapons', 'abilities', 'armor', 'rings', 'etc']

    # Store the item types and their links in dictionaries
    weapons = getLinks('weapons') # {daggers: /wiki/daggers, dual blades: /wiki/dual-blades}
    abilities = getLinks('ability-items')
    armor = getLinks('armor')
    rings = getLinks('rings')

    # Create a dictionary mapping all the category types with their names
    categories = {"Weapons": weapons, "Abilities": abilities, "Armor": armor, "Rings": rings}
    # categories = {"Abilities": abilities}

    # Loop through the dictionary of categories and subcategories and store the items from each link in the database
    for categoryName, category in categories.items(): # Ex: {"Weapons": weapons, "Abilities": abilities, "Armor": armor, "Rings": rings}
        for subCategory, link in category.items(): # Ex: {weapons = daggers: /wiki/daggers, dual blades: /wiki/dual-blades}
            print(f'{categoryName} > {subCategory}: {link}')
            storeItems(link, categoryName, subCategory)

if __name__ == '__main__':
    main()