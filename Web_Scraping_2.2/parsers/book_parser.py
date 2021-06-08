import re
import logging
from locators.book_locators import BookLocators

logger=logging.getLogger('scraping.book_parser')

class Book_Parser:
 RATINGS={
  'One':1,
  "Two":2,
  "Three":3,
  "Four":4,
  "Five":5
  
 }
 def __init__(self,parent):
   logger.debug(f'New book parser created from `{parent}`')
   self.parent=parent
 
 def __repr__(self):
   return f"<Book {self.name} ({self.link}) price at {self.price} with rating of {self.rating}. >"
 
 @property 
 def name(self):
  logger.debug('Finding the book name...')
  locator=BookLocators.NAME_LOCATOR
  item_link=self.parent.select_one(locator)
  item_name=item_link.attrs["title"]
  logger.debug(f'Found book name`{item_name}')
  return item_name

 @property 
 def link(self):
  logger.debug('Finding the book link...')
  locator=BookLocators.LINK_LOCATOR
  item_link=self.parent.select_one(locator).attrs['href']
  logger.debug(f'Found book link`{item_link}')
  return item_link

 @property 
 def price(self):
  logger.debug('Finding the book price...')
  locator=BookLocators.PRICE_LOCATOR
  price=self.parent.select_one(locator).string
  logger.debug(f'Found book price`{price}')
  expression="£([0-9]+\.[0-9])"
  matches=re.search(expression,price)
  return float(matches[1])

 @property 
 def rating(self):
   logger.debug('Finding the book rating...')
   locator=BookLocators.RATING_LOCATOR
   rating_tag=self.parent.select_one(locator).attrs['class']
   rating=[x for x in rating_tag if x!='star-rating'][0]
   logger.debug(f'Found book rating`{rating}')
   rating_number=Book_Parser.RATINGS.get(rating)
   logger.debug(f'translated rating into rating number`{rating_number}')
   return rating_number


