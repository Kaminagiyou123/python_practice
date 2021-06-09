from pages.quotes_page import InvalidTagForAuthorError
from selenium import webdriver
from pages.quotes_page import QuotesPage
try:
 author=input("Enter the author you'd like qutoes from: ")
 tag=input("Enter your tag: ")

 chrome=webdriver.Chrome(executable_path="/Users/ranyou/Downloads/chromedriver")
 chrome.get("https://quotes.toscrape.com/search.aspx")
 page=QuotesPage(chrome)

 print(page.search_for_quotes(author,tag))
 
except InvalidTagForAuthorError as e:
 print(e)
except Exception as e:
 print(e)
 print("An error has occured")
