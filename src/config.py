# src/config.py

"""
Configuration constants for Chrome Tab Saver.
"""

# Chrome DevTools Protocol debug port
DEBUG_PORT = 9222

# Domains to skip when saving tabs
EXCLUDE_DOMAINS = [
    "mail.google.com",
    "calendar.google.com",
]

# OpenAI model & token limits
OPENAI_MODEL = "gpt-3.5-turbo"
MAX_SUMMARY_TOKENS = 200
