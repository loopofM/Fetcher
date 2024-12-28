from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_html(query, location, start):
    """
    Fetch HTML content for a given job search query and location using Selenium.

    Args:
        query (str): Job title or keyword to search for.
        location (str): City or location to search in.
        start (int): The starting index for pagination.

    Returns:
        str: The HTML content of the fetched page.
    """
    options = Options()
    options.headless = True  
    driver = webdriver.Chrome(options=options)
    url = f"https://www.indeed.com/jobs?q={query}&l={location}&start={start}"

    try:
        logging.info(f"Fetching page for query: '{query}', location: '{location}', start: {start}")
        driver.get(url)

        time.sleep(3)  
        html = driver.page_source

        return html
    except Exception as e:
        logging.error(f"Failed to fetch HTML: {e}")
        return None
    finally:
        driver.quit()  
