import re
from typing import List

from bs4 import BeautifulSoup

SEARCH_URLS = {
    "butai": "https://www.aruodas.lt/butai/puslapis/{page_number}/",
    "namai": "https://www.aruodas.lt/namai/puslapis/{page_number}/",
    "patalpos": "https://www.aruodas.lt/patalpos/puslapis/{page_number}/",
    "butu-nuoma": "https://www.aruodas.lt/butu-nuoma/puslapis/{page_number}/",
    "patalpu-nuoma": "https://www.aruodas.lt/patalpu-nuoma/puslapis/{page_number}/",
    "sklypai-pardavimui": "https://www.aruodas.lt/sklypai-pardavimui/puslapis/{page_number}/?FOfferType=1&FBuildingType=1",
    "garazai-pardavimui": "https://www.aruodas.lt/garazai-pardavimui/puslapis/{page_number}/?FOfferType=1&FBuildingType=1",
    "trumpalaike-nuoma": "https://www.aruodas.lt/trumpalaike-nuoma/puslapis/{page_number}/",
}


def get_max_page_number(page_html: str) -> int:
    """Return the maximum page number from the given HTML page."""
    soup = BeautifulSoup(page_html, "html.parser")
    page_numbers = soup.find_all("a", class_="page_bt")
    parsed_numbers = [a.get("href").split("/")[-2] for a in page_numbers]
    return max([int(n) for n in parsed_numbers])


def filter_strings(string_list: List[str]) -> List[str]:
    """Filter out a list of strings, selecting only those who potentially represent RE links."""
    pattern = r"^\d{1,2}-\d{3,}$"
    return [s for s in string_list if re.match(pattern, s)]


def retrieve_re_links(page_html: str) -> List[str]:
    """Retrieve all RE links from the given HTML page."""
    soup = BeautifulSoup(page_html, "html.parser")
    links = soup.find_all("a")
    hrefs = [link.get("href") for link in links]
    return filter_strings(hrefs)
