from scraper.parse import parse_page
from scraper.fetch import fetch_page, start_driver, close_driver
from storage.database import insert_items, count_total_items, drop_items_collection
from typing import List


def run():
    # Parent link
    mainLink: str = "https://www.realmeye.com/wiki/"

    equipment: dict[list] = {
        "weapons": ['daggers', 'dual-blades', 'bows', 'longbows', 'staves', 'spellblades', 'wands', 'morning-stars', 'swords', 'flails', 'katanas', 'tachis'],
        "abilities": ['cloaks', 'quivers', 'spells', 'tomes', 'helms', 'shields', 'seals', 'poisons', 'skulls', 'traps', 'orbs', 'prisms', 'scepters', 'stars', 'wakizashi', 'lutes', 'maces', 'sheaths'],
        "armor": ['leather-armors', 'robes', 'heavy-armors'],
        "rings": ['health-rings', 'magic-rings', 'attack-rings', 'defense-rings', 'speed-rings', 'dexterity-rings', 'vitality-rings', 'wisdom-rings', 'untiered-rings', 'limited-rings'],
        # "shiny-items": ['shiny-items']
    }

    # Optional: Drop existing items collection to start fresh
    drop_items_collection()
    
    # Start the WebDriver once before scraping
    start_driver()
    
    try:
        # Loop through all equipment links to parse through and store information
        for category_name, subcategory_list in equipment.items():
            print(f"\n=== Processing {category_name.upper()} ===")
            
            for subcategory in subcategory_list:
                print(f"\n--- Processing subcategory: {subcategory} ---")
                
                # Fetch and parse the page
                soupData = fetch_page(subcategory)
                parsedData = parse_page(soupData)
                
                # Insert parsed data into MongoDB
                if parsedData:
                    insert_items(parsedData, subcategory, category_name)
                else:
                    print(f"No items found for subcategory: {subcategory}")
        
        # Print total items count at the end
        print(f"\n--- Scraping Complete ---")
        count_total_items()
                
    finally:
        # Always close the driver, even if an error occurs
        close_driver()

    


# Run run() when executed directly
if __name__ == "__main__":
    run()
