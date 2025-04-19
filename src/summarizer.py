# src/summarizer.py

"""
summarizer.py
Wraps OpenAI API calls to generate 2–3 line summaries.
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from src.config import OPENAI_MODEL, MAX_SUMMARY_TOKENS


def summarize_text(text: str, max_tokens: int = MAX_SUMMARY_TOKENS) -> str:
    """
    Call OpenAI to produce a brief summary of `text`.
    """
    if not text:
        return "(No text to summarize)"

    try:
        resp = client.chat.completions.create(model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes web pages in 2-3 lines."},
            {"role": "user", "content": text}
        ],
        max_tokens=max_tokens,
        temperature=0.5)
        return resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"Warning: summarization failed: {e}")
        return "(Summary unavailable)"
