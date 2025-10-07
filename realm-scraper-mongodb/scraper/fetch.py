# fetch.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# chrome_options.add_argument("--headless=new")  # faster, modern headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")


class WebDriverManager:
    """Manages a single Chrome WebDriver instance for multiple page fetches"""
    
    def __init__(self):
        self.driver = None
    
    def start_driver(self):
        """Initialize the Chrome driver"""
        if self.driver is None:
            print("Starting Chrome WebDriver...")
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), 
                options=chrome_options
            )
    
    def fetch_page(self, subcategory: str) -> str:
        """
        Fetches the HTML of a RealmEye wiki page using the existing driver
        """
        if self.driver is None:
            self.start_driver()
        
        url = f"https://www.realmeye.com/wiki/{subcategory}"
        print(f"Fetching: {url}")
        
        self.driver.get(url)
        html = self.driver.page_source
        
        return html
    
    def close_driver(self):
        """Close the Chrome driver"""
        if self.driver:
            print("Closing Chrome WebDriver...")
            self.driver.quit()
            self.driver = None


class WebDriverContextManager:
    """Context manager for Chrome WebDriver - use with 'with' statement"""
    
    def __init__(self):
        self.driver = None
    
    def __enter__(self):
        print("Starting Chrome WebDriver...")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=chrome_options
        )
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            print("Closing Chrome WebDriver...")
            self.driver.quit()
    
    def fetch_page(self, subcategory: str) -> str:
        """Fetch a page using the context manager's driver"""
        url = f"https://www.realmeye.com/wiki/{subcategory}"
        print(f"Fetching: {url}")
        
        self.driver.get(url)
        return self.driver.page_source


# Global instance for backwards compatibility
_driver_manager = WebDriverManager()

def fetch_page(subcategory: str) -> str:
    """
    Fetches the HTML of a RealmEye wiki page using Selenium
    (backwards compatible function)
    """
    return _driver_manager.fetch_page(subcategory)

def start_driver():
    """Start the global driver instance"""
    _driver_manager.start_driver()

def close_driver():
    """Close the global driver instance"""
    _driver_manager.close_driver()