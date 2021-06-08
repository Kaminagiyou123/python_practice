import logging
from app import books

logger=logging.getLogger('scraping.menu')
def print_best_books():
 logger.info("Finging the best books by rating...")
 best_books=sorted(books,key=lambda x:x.rating*-1)[:5]
 for book in best_books:
   print(book)
def print_cheap_books():
 logger.info("Finging the cheap books by price...")
 cheap_books=sorted(books,key=lambda x:x.price)[:5]
 for book in cheap_books:
   print(book)
     
books_generator=(x for x in books)
def print_next_book():
 logger.info("Finging the next book...")
 print(next(books_generator))
 
def menu():
 user_input=input("Enter your choice: ")
 while user_input!="q":
  if user_input=="b":
   print_best_books()
  elif user_input=="c":
   print_cheap_books()
  elif user_input=="n":
   print_next_book()
  user_input=input("Enter your choice: ")

menu()