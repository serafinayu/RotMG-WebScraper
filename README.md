# Realmeye Item Scraper

## About

This is a webscraper that scrapes equipment data from the RotMG official wiki page (realmeye.com). The collected equipment data consists of item names, img urls, tiers, categories, and subcategories.

## Purpose

This webscraper was built for personal use to populate data needed for my RotMG Loot Tracker web app.

## Usage

Only the `realm-scraper-mongodb/` project is currently functioning as of Oct 2025. The `realm-scraper-psql` is a legacy version that has not been updated.

1. Clone this repo to your device
2. Change directories to the `realm-scraper-mongodb/`
3. Create a cluster in MongoDB and get the connection string for it
4. Ensure you create a database user and set a password in MongoDB
   - Make sure to update your connection string with the database user credentials
5. Create a `.env` file within your directory and insert the following:

```env
MONGODB_URI = <your_connection_string_from_mongodb>
DB_NAME = <name_of_your_database>
```

6. Run `./run.sh` in you terminal
