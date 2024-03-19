from configparser import ConfigParser

"""
    This file creates a config file
"""

# Create an instance of the config parser
config = ConfigParser()

# Create a default config setting with the database info
config["DEFAULT"] = {
    "database": "rotmg-ssnl-loot", 
    "user": "rotmg", 
    "host": 'localhost',
    "password": "realm",
    "port": 5432
}

# When the config file is opened, write it to a config file called config.ini
with open("config.ini", "w") as f:
    config.write(f)