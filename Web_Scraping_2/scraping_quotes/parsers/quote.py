from locators.quote_locators import QuoteLocators
import re
class QuoteParser:
 def __init__(self,parent):
  self.parent=parent
  
 def __repr__(self):
  return f"<Book {self.name} ({self.link}) price at {self.price} with rating of {self.rating}. >"
 
 @property
 def name(self):
  locator=QuoteLocators.NAME_LOCATOR
  item_link=self.parent.select_one(locator)
  item_name=item_link.attrs["title"]
  return item_name
 
 @property
 def link(self):
  locator=QuoteLocators.LINK_LOCATOR
  item_link=self.parent.select_one(locator).attrs['href']
  return item_link
 
 @property
 def price(self):
  locator=QuoteLocators.PRICE_LOCATOR
  price=self.parent.select_one(locator).string
  expression="£([0-9]+\.[0-9])"
  matches=re.search(expression,price)
  return float(matches[1])
 
 @property
 def rating(self):
   locator=QuoteLocators.RATING_LOCATOR
   rating_tag=self.parent.select_one(locator).attrs['class']
   rating=[x for x in rating_tag if x!='star-rating'][0]
   return rating
  