# Dev Log

## **10/7/2025**

I originally created a locally run version of this project. My first attempt I used BeautifulSoup to scrape the data and stored the data in a local postgres database. Flask API was used to query data from the locally hosted database.

In my second attempt, I used the same webscraper I originally made and had it store item data in a mongodb database. From there I hosted the Flask API on Vercel but had issues querying data from subcategories that had a space character in it. I took a break after running into this wall and have finally come back to it after working on a UI for my RotMG Loot Tracker project.

The current version of the webscraper uses Selenium to pull the html data from the wiki. It seems RotMG uses Cloudflare to prevent bots from accessing the site data. I didn't have any luck pulling the data by passing different headers when making requests, and neither did I get any positive results when I used libraries like `cloudscraper`. It only seemed to work when I ran it with Selenium. I also tried to run Selenium headless, but to no avail. Even with libraries like `undetected_chromedriver`, running Selenium headless would fail to load the page's html fully.

## **2024**

Flask API that returns basic item info from the game Realm of the Mad God in json. This API will be used in my Seasonal Loot Counter for Realm of the Mad God, allowing players to update what loot they obtained throughout the season. This API can be run locally via `realm-scraper-psql` or through Vercel via `realm-scraper-mongo`.

---

### API Endpoints:

- Get all items: `/items/`
- Get items by category: `/items/<category-name>/`
- Get items by category and subcategory: `/items/<category-name>/<subcategory-name>`
- Get items by searching by name: `/items/search/<some-string>`

#### Possible Categories:

- Categories: Weapons, Abilities, Armor, Rings
- Subcategories:
  - Weapons: Daggers, Dual Blades, Bows, Longbows, Staves, Spellblades, Wands, Morning Stars, Swords, Flails, Katanas, Tachis
  - Abilities: Cloaks, Quivers, Spells, Tomes, Helms, Shields, Seals, Poisons, Skulls, Traps, Orbs, Prisms, Scepters, Stars, Wakizashi, Lutes, Maces, Sheaths
  - Armor: Leather Armors, Robes, Heavy Armors
  - Rings: Health Rings, Magic Rings, Attack Rings, Defense Rings, Speed Rings, Dexterity Rings, Vitality Rings, Wisdom Rings, Untiered Rings, Limited Rings
