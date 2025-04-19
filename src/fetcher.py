# src/fetcher.py

"""
fetcher.py
Provides functions to download a web page and extract its main text.
"""

import requests
from bs4 import BeautifulSoup

def fetch_page_text(url: str, max_paragraphs: int = 5) -> str:
    """
    Download the page at `url` and return up to `max_paragraphs` of text.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join(p.get_text() for p in paragraphs[:max_paragraphs])
    except Exception as e:
        print(f"Warning: failed to fetch {url}: {e}")
        return ""
