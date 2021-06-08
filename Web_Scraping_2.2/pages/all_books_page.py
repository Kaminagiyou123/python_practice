import re
import logging
from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import Book_Parser

logger=logging.getLogger('scraping.all_books_page')

class AllBookPage:
 def __init__(self,page_content):
  logger.debug('Parsng page content with Beautiful Soup html parser')
  self.soup= BeautifulSoup(page_content,'html.parser')
 
 @property
 def book(self):
  logger.debug(f'finding all books in the page using `{AllBooksPageLocators.BOOKS}`')
  return [ Book_Parser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS) ]
 
 @property
 def page_count(self):
  
  content=self.soup.select_one(AllBooksPageLocators.PAGER).string
  expression="Page [0-9] of ([0-9]+)"
  logger.debug(f'finding the number of catalog pages available `{content}`')
  matches=re.search(expression,content)
  return int(matches[1])
 
