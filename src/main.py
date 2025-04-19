# src/main.py

"""
Entry point for Chrome Tab Saver.
Gathers open Chrome tabs and writes a Markdown report.
"""

from datetime import datetime
import pychrome

from src.config import DEBUG_PORT, EXCLUDE_DOMAINS
from src.fetcher import fetch_page_text
from src.summarizer import summarize_text

def get_chrome_tabs(port: int = DEBUG_PORT):
    browser = pychrome.Browser(url=f"http://127.0.0.1:{port}")
    return browser.list_tab()

def write_markdown_report(tabs):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"chrome_tabs_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.md"
    with open(filename, "w", encoding="utf-8") as md:
        md.write(f"# Chrome Tabs Session - {timestamp}\n\n")
        for tab in tabs:
            url = tab.url
            if any(domain in url for domain in EXCLUDE_DOMAINS):
                continue
            title = tab.title or url
            print(f"Processing: {title}")
            page_text = fetch_page_text(url)
            summary = summarize_text(page_text) if page_text else "(Failed to extract text)"
            md.write(f"## {title}\n")
            md.write(f"[{url}]({url})\n\n")
            md.write(f"{summary}\n\n---\n\n")
    print(f"Report generated: {filename}")

def main():
    tabs = get_chrome_tabs()
    write_markdown_report(tabs)

if __name__ == "__main__":
    main()
