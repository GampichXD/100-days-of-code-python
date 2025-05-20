# Professional Portfolio Project - Web Scraping
# Custom Web Scrapper
# Author : Abraham
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.audible.com/search"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_page(page=1):
    params = {
        "keywords": "Science",
        "page": page
    }

    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select(".productListItem")
    data = []

    for book in books:
        title = book.select_one(".bc-list-item h3").get_text(strip=True) if book.select_one(".bc-list-item h3") else "N/A"
        author = book.select_one("li.authorLabel span a").get_text(strip=True) if book.select_one("li.authorLabel span a") else "N/A"
        narrator = book.select_one("li.narratorLabel span a").get_text(strip=True) if book.select_one("li.narratorLabel span a") else "N/A"
        length = book.select_one("li.runtimeLabel span").get_text(strip=True) if book.select_one("li.runtimeLabel span") else "N/A"
        release_date = book.select_one("li.releaseDateLabel span").get_text(strip=True) if book.select_one("li.releaseDateLabel span") else "N/A"
        lang = book.select_one("li.languageLabel span").get_text(strip=True) if book.select_one("li.languageLabel span") else "N/A"
        rating = book.select_one(".ratingsLabel .bc-pub-offscreen")
        rating_val = rating.get_text(strip=True) if rating else "N/A"

        data.append({
            "Title": title,
            "Author": author,
            "Narrator": narrator,
            "Length": length,
            "Release Date": release_date,
            "Language": lang,
            "Rating": rating_val
        })

    return data

def scrape_multiple_pages(num_pages=3):
    all_data = []
    for page in range(1, num_pages + 1):
        print(f"Scraping page {page}...")
        page_data = scrape_page(page)
        all_data.extend(page_data)
    return all_data

# Run and save to CSV
books_data = scrape_multiple_pages(3)
df = pd.DataFrame(books_data)
df.to_csv("../Day 93 PPP - Web Scraping/audible_books.csv", index=False)
print("Saved to 'audible_books.csv'")






