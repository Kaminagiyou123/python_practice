from app import books

def print_best_books():
 best_books=sorted(books,key=lambda x:x.rating*-1)[:5]
 for book in best_books:
   print(book)
def print_cheap_books():
 cheap_books=sorted(books,key=lambda x:x.price)[:5]
 for book in cheap_books:
   print(book)
     
books_generator=(x for x in books)
def print_next_book():
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