import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(base_url, pages=1):
    all_books = []

    for page in range(1, pages + 1):
        url = f"{base_url}/catalogue/page-{page}.html"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a['title']
            price_text = book.find('p', class_='price_color').text
            price_clean = price_text.encode('ascii', 'ignore').decode().strip().replace('£', '')
            rating = book.p.get('class')[1]
            availability = book.find('p', class_='instock availability').text.strip()


            all_books.append({
                'Title': title,
                'Price (£)': float(price_clean),
                'Rating': rating,
                'Availability': availability
            })


    return pd.DataFrame(all_books)
