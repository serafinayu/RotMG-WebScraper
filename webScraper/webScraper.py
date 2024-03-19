from links import getLinks
from items import storeItems

def main():
    # item-category-types
    itemCategory = ['weapons', 'abilities', 'armor', 'rings', 'etc']

    # Store the item types and their links in dictionaries
    weapons = getLinks('weapons') # {daggers: /wiki/daggers, dual blades: /wiki/dual-blades}
    abilities = getLinks('ability-items')
    armor = getLinks('armor')
    rings = getLinks('rings')

    # categories = {"Weapons": weapons, "Abilities": abilities, "Armor": armor, "Rings": rings}
    categories = {"Abilities": abilities}
    for categoryName, category in categories.items(): # Ex: {"Weapons": weapons, "Abilities": abilities, "Armor": armor, "Rings": rings}
        for subCategory, link in category.items(): # Ex: {weapons = daggers: /wiki/daggers, dual blades: /wiki/dual-blades}
            print(f'{categoryName} > {subCategory}: {link}')
            storeItems(link, categoryName, subCategory)

    # Now that I have the links, I need to pull each item's info from those pages and store them in the database
        # tbody > tr > only need the first three a tags {1: img, 2: tier, 3: name}
        # bool first = true
            # if true: go one level deeper to get img tag's src link
            # if false: get text of the a tag
            # if false: get text of the a tag
    # Send the item types and links to their respective functions 
    # Send and store the deafault item info in the database
    # Need to make an API to make endpoints to change the amount of each item obtaines
    # Need to make endpoints that query for certain information when needed


if __name__ == '__main__':
    main()