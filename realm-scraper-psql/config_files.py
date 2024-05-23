from configparser import ConfigParser

"""
This module provides a function to create the config file. My program would probably be
better without this file and just need a config file, but I wanted to learn how to use
ConfigParser to create a config file.
"""

def create_config():
    """Creates the config file with data used to connect to the database"""
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
    with open("./config.ini", "w") as f:
        config.write(f)