import requests
from pages.quotes_page import QuotesPage

page_content=requests.get("https://books.toscrape.com/")
page=QuotesPage(page_content)

for book in page.quotes:
 print(book)