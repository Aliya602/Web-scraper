# Web-scraper 🌐
A web scaper-written in Python, that extracts quotes, quthors, tags, and author birthdays [quotes.toscrape.com](http://quotes.toscrape.com)- a website designed for practicing web scraping

## Features
## Basic Scapper('Web_scraper_basics.py')
- ☑️ Scrapes 100 quotes from 10 pages
- ☑️ Extracts quote text, author name, and tags
- ☑️ Saves data to `quotes.json`


## Adavnced Scraper ('Web_scraper_with_birthday.py')
- ☑️ Scrapes 100 quotes from 10 pages
- ☑️ Extracts quote text, author name, and tags
- ☑️ Follows author links to scape birthdates
- ☑️ Combines data from two sources
-  ☑️ Saves data to `quotes_with_birthdays.json`

## Tech stack
- `requests` - Download web pages online
- `BeautifulSoup` - Parse HTML and extract data
- `json`- Save data to JSON files
- `time` - Polite delays between requests

## What I Learned during this project
- How to scrape paginated websites
- How to follow links to scrape  related pages
- How to combine data from multiple sources
- How to be polite with `time.sleep()`
- How to handle errors with try/except

## How to Run

### Install dependencies:
```bash
pip install requests beautifulsoup4
