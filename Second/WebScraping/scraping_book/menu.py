from app import books

USER_CHOICE=""" Enter one of the following
_"b" to look at 5-star books
_"c" to look at cheapest books
_"n" to just get the next available book on the catalog
_"q" to quit
"""

def print_best_books():
 best_books=sorted(books,key=lambda x:x.rating *-1)[:5]
 for book in best_books:
  print(book)
  
def print_cheapest_books():
  cheapest_books=sorted(books,key=lambda x:x.price)[:10]
  for book in cheapest_books:
   print(book)
 
def print_next_book():
  next_book=(x for x in books)
  print(next(next_book))

print(USER_CHOICE)
Input=input("Enter your input: ")
while Input!='q':
  if Input=='b':
    print_best_books()
  elif Input=='c':
    print_cheapest_books()
  elif Input=='n':
    print_next_book()
  Input=input("Enter your input: ")