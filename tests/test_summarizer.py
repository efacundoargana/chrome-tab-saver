# tests/test_summarizer.py

"""
Simple unit test for summarize_text.
"""

import os
import openai
from src.summarizer import summarize_text

class DummyResp:
    choices = [type("C", (), {"message": type("M", (), {"content": "Test summary."})()})]

def test_summarize_text(monkeypatch):
    # Ensure API key is present
    monkeypatch.setenv("OPENAI_API_KEY", "fake_key")

    # Mock the OpenAI call
    def mock_create(**kwargs):
        return DummyResp()
    monkeypatch.setattr(openai.ChatCompletion, "create", staticmethod(mock_create))

    result = summarize_text("Some test text.")
    assert result == "Test summary."
