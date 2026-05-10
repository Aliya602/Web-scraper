# importing necessary libraries
import requests
import json
import time
from bs4 import BeautifulSoup


all_quotes = []
page_number = 1

# Loop through pages until we hit a 404 or no quotes are found
while True:
    url = f"http://quotes.toscrape.com/page/{page_number}/"
    print(f"📜 Scraping page {page_number}...")
    response = requests.get(url)

    if response.status_code == 404:
        print(f"Page {page_number} not found. Stopping.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if not quotes:
        break

    print(f'Found {len(quotes)} quotes on page {page_number}')

    # Process each quote on this page using a for loop
    for quote in quotes:
        quote_text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    # Get auothers quote and tags
        all_quotes.append({
            'quote': quote_text,
            'author': author,
            'tags': tags
        })

        # Print progress
        print(f'  Quote 💐: {quote_text[:80]}...')  # Show first 80 chars only
        print(f'  Author: {author}')
        print(f'  Tags: {", ".join(tags)}\n')

    # time delay to be polite to the server (1 second)
    time.sleep(1)
    page_number += 1

with open('quotes.json', 'w') as file:
    json.dump(all_quotes, file, indent=2)

print(f"\n✅ Saved {len(all_quotes)} quotes to quotes.json")
