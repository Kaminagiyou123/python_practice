import re
from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import Book_Parser

class AllBookPage:
 def __init__(self,page_content):
  self.soup= BeautifulSoup(page_content,'html.parser')
 
 @property
 def book(self):
  return [ Book_Parser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS) ]
 
 @property
 def page_count(self):
  content=self.soup.select_one(AllBooksPageLocators.PAGER).string
  expression="Page [0-9] of ([0-9]+)"
  matches=re.search(expression,content)
  return int(matches[1])
 
