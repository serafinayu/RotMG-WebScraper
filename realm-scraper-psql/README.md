# The files in this folder are a variation of the realmeye scraper that uses and stores item info in a local PSQL database. 

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
