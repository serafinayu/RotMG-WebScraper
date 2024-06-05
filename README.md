# Realmeye Item Scraper
This is a Flask API that returns basic item info from the game Realm of the Mad God in json. This API will be used in my Seasonal Loot Counter for Realm of the Mad God, allowing players to update what loot they obtained throughout the season. This API can be run locally via `realm-scraper-psql` or through Vercel via `realm-scraper-mongo`. 

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
      