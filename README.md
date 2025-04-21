# AI Web Scraper with Browser Use + Gemini

This project is a general-purpose autonomous web-scraping agent powered by [browser-use](https://github.com/Browser-Use/browser-use) and Google Cloud’s Gemini 1.5 Pro model. It enables you to define flexible natural language tasks such as:

- Navigating to a website  
- Searching or interacting with page elements  
- Extracting structured data like titles, URLs, descriptions, etc.

This is especially effective for scraping dynamically loaded websites such as YouTube, Reddit, Google Search, and others that rely on JavaScript rendering.

---

## Features

- Autonomous agent behavior driven by LLM prompts  
- Embedded browser automation using Playwright via `browser-use`  
- Structured JSON output parsing with Pydantic  
- Robust handling of JavaScript-heavy pages  
- General-purpose prompt-driven task definition  
- Optional model swapping (e.g., Claude, Ollama, GPT, etc.)

---

## Requirements

- Python 3.9 or higher  
- Google Chrome (installed locally)  
- Google Cloud Gemini API key  
  - Or your own LLM-compatible API (Claude, Ollama, GPT, etc.)

---

## Installation

```bash
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
