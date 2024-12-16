from bs4 import BeautifulSoup
import logging

def parse_jobs(html):
    """
    Parse job listings from the HTML content.

    Args:
        html (str): HTML content.

    Returns:
        list[dict]: A list of job postings, each as a dictionary.
    """

    soup = BeautifulSoup(html, 'html.parser')
    job_cards = soup.select(".job_seen_bacon") # CSS selector for job cards
    jobs = []

    for card in job_cards:
        try:
            title = card.find("h2", class_="jobTitle").text.strip()
            company = card.find("span", class_="companyName").text.strip()
            location = card.find("div", class_="companyLocation").text.strip()
            salary = card.find("div", class_="salary-snippet")
            salary = salary.text.strip() if salary else "Not specified"
            summary = card.find("div", class_="job-snippet").text.strip()

            jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Salary": salary,
                "Summary": summary
            })
        except Exception as e:
            logging.warning(f"Failed to parse a job card: {e}")

    return jobs
