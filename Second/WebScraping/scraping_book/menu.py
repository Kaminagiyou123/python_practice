from app import books

def print_best_books():
 best_books=sorted(books,key=lambda x:x.rating *-1)[:5]
 for book in best_books:
  print(book)
 
print_best_books()