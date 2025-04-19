# src/main.py

from datetime import datetime
from src.chrome_tabs import get_chrome_tabs
from src.config import EXCLUDE_DOMAINS
from src.fetcher import fetch_page_text
from src.summarizer import summarize_text

def write_markdown_report(tabs):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"chrome_tabs_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.md"
    with open(filename, "w", encoding="utf-8") as md:
        md.write(f"# Chrome Tabs Session - {timestamp}\n\n")
        for tab in tabs:
            url = tab["url"]
            if any(domain in url for domain in EXCLUDE_DOMAINS):
                continue
            title = tab["title"]
            print(f"Processing: {title}")
            text = fetch_page_text(url)
            summary = summarize_text(text) if text else "(Failed to extract text)"
            md.write(f"## {title}\n")
            md.write(f"[{url}]({url})\n\n")
            md.write(f"{summary}\n\n---\n\n")
    print(f"Report generated: {filename}")

def main():
    # on macOS this grabs your live session; elsewhere you need --remote-debugging-port
    tabs = get_chrome_tabs(port=None)  
    write_markdown_report(tabs)

if __name__ == "__main__":
    main()
