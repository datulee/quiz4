import requests
from bs4 import BeautifulSoup
import csv
import time


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    book_titles = soup.find_all('h5', class_='mkdf-product-list-title')
    book_authors = soup.find_all('a', class_='mkdf-pl-author-holder')
    book_prices = soup.find_all('span', class_='woocommerce-Price-amount amount')

    with open('books.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for title, author, price in zip(book_titles, book_authors, book_prices):
            book_title = title.text.strip()
            book_author = author.text.strip()
            book_price = price.text.strip().replace("&nbsp;","")
            writer.writerow([book_title, book_author, book_price])


def scrape_multiple_pages():
    page_number = 1

    while page_number<6:
        url = f'https://www.sulakauri.ge/wignebi/?product-page={page_number}'
        scrape_page(url)
        time.sleep(15)
        page_number += 1


scrape_multiple_pages()
