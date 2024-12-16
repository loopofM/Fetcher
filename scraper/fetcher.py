from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time

# Configure logging
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
    # Configure the Chrome options for headless mode (runs the browser in the background)
    options = Options()
    options.headless = True  # Enable headless mode (no UI)

    # Set path to your ChromeDriver
    driver = webdriver.Chrome(options=options)

    # Construct the URL with pagination
    url = f"https://www.indeed.com/jobs?q={query}&l={location}&start={start}"

    try:
        logging.info(f"Fetching page for query: '{query}', location: '{location}', start: {start}")
        driver.get(url)

        # Wait for the page to load (can be adjusted if necessary)
        time.sleep(3)  # Give some time for the page to fully render (increase if necessary)

        # Get the page source after the JavaScript loads
        html = driver.page_source

        return html
    except Exception as e:
        logging.error(f"Failed to fetch HTML: {e}")
        return None
    finally:
        driver.quit()  # Close the browser after fetching the page
