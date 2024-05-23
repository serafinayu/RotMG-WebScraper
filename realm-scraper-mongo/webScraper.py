# from connection import create_db
from links import getLinks
from items import storeItems, insertItems
import connection

def main():
    # Delete the database collection if it exists
    connection.drop_items_collection()

    # Store the item types and their links in dictionaries
    weapons = getLinks('weapons') # {daggers: /wiki/daggers, dual blades: /wiki/dual-blades}
    abilities = getLinks('ability-items')
    armor = getLinks('armor')
    rings = getLinks('rings')
    items = []

    # Create a dictionary mapping all the category types with their names
    categories = {"Weapons": weapons, "Abilities": abilities, "Armor": armor, "Rings": rings}
    # categories = {"Abilities": abilities}

    # Loop through the dictionary of categories and subcategories and store the items from each link in the database
    for categoryName, category in categories.items(): # Ex: {"Weapons": weapons, "Abilities": abilities, "Armor": armor, "Rings": rings}
        for subCategory, link in category.items(): # Ex: {weapons = daggers: /wiki/daggers, dual blades: /wiki/dual-blades}
            print(f'{categoryName} > {subCategory}: {link}')
            items += storeItems(link, categoryName, subCategory)

    insertItems(items)
    # print(items)

if __name__ == '__main__':
    main()