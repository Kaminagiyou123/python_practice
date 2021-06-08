import requests
import logging

from pages.all_books_page import AllBookPage


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger=logging.getLogger('scraping')

logger.debug("Loading books list...")

page_cotent=requests.get("https://books.toscrape.com/").content;
page=AllBookPage(page_cotent)

books=page.book;
max_num=page.page_count

for page_num in range(1,max_num):
 url=f'https://books.toscrape.com/catalogue/page-{page_num}.html'
 page_cotent=requests.get(url).content;
 page=AllBookPage(page_cotent)
 books.extend(page.book)
 
 
