# Realmeye Item Scraper
This is a Flask API that returns basic item info from the game Realm of the Mad God in json. I built this with plans on creating a Seasonal Loot Counter for Realm of the Mad God, allowing players to update what loot they obtained throughout the season. Currently this is built to run on a local server. I plan to recreate this but using MongoDB instead since I do not have a dedicated server as of now. 

---
## API Endpoints:
- Get all items: `/items/`
- Get items by category: `/items/<category-name>/`
- Get items by category and subcategory: `/items/<category-name>/<subcategory-name>`
- Get items by searching by name: `/items/search/<some-string>`

### Possible Categories:
- Categories: Weapons, Abilities, Armor, Rings
- Subcategories:
    - Weapons: Daggers, Dual Blades, Bows, Longbows, Staves, Spellblades, Wands, Morning Stars, Swords, Flails, Katanas, Tachis
    - Abilities: Cloaks, Quivers, Spells, Tomes, Helms, Shields, Seals, Poisons, Skulls, Traps, Orbs, Prisms, Scepters, Stars, Wakizashi, Lutes, Maces, Sheaths
    - Armor: Leather Armors, Robes, Heavy Armors
    - Rings: Health Rings, Magic Rings, Attack Rings, Defense Rings, Speed Rings, Dexterity Rings, Vitality Rings, Wisdom Rings, Untiered Rings, Limited Rings
      
---

### Run this program on your system:
Requirements: Operating System  Ubuntu 22.04
1. Update system: `sudo apt update`
2. Create a PostgreSQL server, user, and database
    - Install PostgreSQL server: `sudo apt install postgresql -y`
    - Create PostgreSQL user: `sudo su - postgres -c "createuser -s rotmg --pwprompt"`
        - Set password to `realm` (If you change the password to something else, make sure to update config_files.py)
    - Create the database: `sudo -u postgres psql -c "CREATE DATABASE \"rotmg-ssnl-loot\" WITH OWNER rotmg;"`
3. Install Python3 and Python3 virtual environment
    - Install Python3 and virtual environment: `sudo apt install python3 python3-venv`
4. Run the run.sh file to start the API: `sh run.sh`

---

### Dependencies
- psycopg2-binary - Used to connect Python to existing database on PostgreSQL server. Originally was using psycopg2 but realized it requires other dependencies that not all environments have. The binary version does not require extra dependencies making it more compatible on other devices.
- requests - Used with BeautifulSoup to scrape data from web pages.
- bs4 - This is the BeautifulSoup library which allows me to web scrape pages
- Flask - Used to create the API endpoints
