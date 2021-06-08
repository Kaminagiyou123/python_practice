import requests

from pages.all_books_page import AllBookPage

page_cotent=requests.get("https://books.toscrape.com/").content;

page=AllBookPage(page_cotent)

books=page.book;

for book in books:
 print(book)