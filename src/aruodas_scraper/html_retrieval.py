import os

import requests

SCRAPING_SERVICE_URL = os.getenv(
    "SCRAPING_SERVICE_URL", "http://0.0.0.0:8000/ai/scrape"
)


def scrape_url(url: str, scraping_service_url: str = SCRAPING_SERVICE_URL) -> str:
    """Scrape the HTML content of a given URL.

    Args:
        url (str): URL to scrape
        scraping_service_url (str): URL of the scraping service

    Returns:
        str: HTML content of the URL
    """
    body = {"url": url}
    response = requests.get(scraping_service_url, json=body)
    return response.json()["html"]
