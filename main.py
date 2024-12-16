from scraper.fetcher import fetch_html
from scraper.parser import parse_jobs
from scraper.exporter import export_to_csv

def main():
    query = "Data Scientist"
    location = ("New York")
    pages_to_scrape = 20

    all_jobs = []

    for page in range(pages_to_scrape):
        start = page * 10
        html = fetch_html(query, location, page)
        if html:
            jobs = parse_jobs(html)
            all_jobs.extend(jobs)

    if all_jobs:
        export_to_csv(all_jobs)
    else:
        print("No jobs found")

if __name__ == "__main__":
    main()