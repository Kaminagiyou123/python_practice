import requests
from bs4 import BeautifulSoup

page=requests.get("https://quotes.toscrape.com/")


class ParsedItemLocators:
 QUOTE_LOCATOR='div.container div.row div.col-md-8 div.quote span.text'
 AUTHOR_LOCATOR='div.container div.row div.col-md-8 div.quote span small.author'


class ParseItem:
 def __init__(self,page):
  self.soup=BeautifulSoup(page.content,'html.parser')
 
  
 def quote(self):
  locator=ParsedItemLocators.QUOTE_LOCATOR
  item_link=self.soup.select(locator)
  quotes=[l.string for l in item_link]
  return quotes
 
 def author(self):
  locator=ParsedItemLocators.AUTHOR_LOCATOR
  item_link=self.soup.select(locator)
  authors=[l.string for l in item_link]
  return authors
 
quotes=ParseItem(page).quote();
author=ParseItem(page).author();
info= list(zip(quotes,author))
print(info)

 

