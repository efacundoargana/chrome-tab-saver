# src/chrome_tabs.py

"""
chrome_tabs.py
Provides get_chrome_tabs() which on macOS uses AppleScript to grab
the current live Chrome session, otherwise falls back to DevTools Protocol.
"""

import platform
import subprocess
from typing import List, Dict

# we'll only import pychrome if needed
def get_chrome_tabs(port: int = None) -> List[Dict[str, str]]:
    """
    Returns a list of tabs, each as {"title": ..., "url": ...}.
    On macOS: uses AppleScript against your running Chrome.
    Else: connects to CDP at localhost:port (requires Chrome launched
    with --remote-debugging-port).
    """
    if platform.system() == "Darwin":
        return _get_tabs_macos()
    else:
        # lazy import so non-mac users don't need osascript
        import pychrome
        browser = pychrome.Browser(url=f"http://127.0.0.1:{port}")
        tabs = browser.list_tab()
        return [
            {"title": tab.title or tab.url, "url": tab.url}
            for tab in tabs
        ]

def _get_tabs_macos() -> List[Dict[str, str]]:
    """
    Uses AppleScript to pull every window/tab from Google Chrome.
    """
    apple_script = '''
    set output to ""
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                set output to output & (title of t) & "||| " & (url of t) & "\n"
            end repeat
        end repeat
    end tell
    return output
    '''
    p = subprocess.Popen(
        ["osascript", "-e", apple_script],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    out, _ = p.communicate()
    lines = out.decode("utf-8").splitlines()
    tabs = []
    for line in lines:
        if "||| " in line:
            title, url = line.split("||| ", 1)
            tabs.append({"title": title.strip(), "url": url.strip()})
    return tabs
