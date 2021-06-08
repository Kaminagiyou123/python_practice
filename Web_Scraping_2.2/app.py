import requests

from pages.all_books_page import AllBookPage

page_cotent=requests.get("https://books.toscrape.com/").content;

page=AllBookPage(page_cotent)

books=page.book;
max_num=page.page_count

for page_num in range(1,max_num):
 url=f'https://books.toscrape.com/catalogue/page-{page_num}.html'
 page_cotent=requests.get(url).content;
 page=AllBookPage(page_cotent)
 books.extend(page.book)
 
 
