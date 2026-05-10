# importing necessary libraries
import requests
import json
import time
from bs4 import BeautifulSoup

# birthday function to fetch author's birthday from their page
def get_author_birthday(author_url):
    try:
        response = requests.get(author_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        birthday_element = soup.find('span', class_='author-born-date')
        if birthday_element:
            return birthday_element.text
        else:
            return "Birthday not found"
    except Exception as e:
        return f"Error: {e}"

all_quotes = []
page_number = 1

while True:
    url = f"http://quotes.toscrape.com/page/{page_number}/"
    print(f"\nScraping page {page_number}...")
    response = requests.get(url)

    if response.status_code == 404:
        print(f"Page {page_number} not found. Stopping.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if not quotes:
        break

    print(f'Found {len(quotes)} quotes on page {page_number}')

    # Process each quote on this page using a for loop (birthday fetching added)
    for quote in quotes:
        quote_text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        author_url = quote.find('a')['href']
        full_author_url = f"http://quotes.toscrape.com{author_url}"
        
        # Fetch the author's birthday
        birthday = get_author_birthday(full_author_url)
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        all_quotes.append({
            'quote': quote_text,
            'author': author,
            'birthday': birthday,
            'tags': tags
        })

       
        # Print progress
        print(f'  Quote: {quote_text[:80]}...')  # Show first 80 chars only
        print(f'  Author: {author}')
        print(f'  Birthday: {birthday}')
        print(f'  Tags: {", ".join(tags)}\n')

        
        time.sleep(0.5)  # Polite delay between author requests

    time.sleep(1)
    page_number += 1

with open('quotes_with_birthdays.json', 'w') as file:
    json.dump(all_quotes, file, indent=2)

print(f"\n✅ Saved {len(all_quotes)} quotes to quotes_with_birthdays.json")