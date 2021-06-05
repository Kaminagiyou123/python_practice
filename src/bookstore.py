import sys
sys.path.insert(0, '../src')
from file_operation import save_to_file

class Book:
 def __init__(self,name,author):
  self.name=name;
  self.author=author;
  self.read=False;
  
 def __repr__(self): 
  return f'{self.name},{self.author},{self.read}'
   
 def mark_book_read(self):
  self.read=True;
  print(f"{self.name} is marked read")
 def unmark_book(self):
  self.read=False;
  print(f"{self.name} is marked un-read")
  

class Bookstore:
 def __init__(self) :
     self.books=[];
 def __repr__(self):
  str="\n".join([ repr(book) for book in self.books])
  return str
 
 def mark_book_read(self,name):
  for book in self.books:
    if book['name']==name:
     book.mark_book_read();
     save_to_file(repr(self),"book.txt")
     return;
  print (f"Book {name} not found in the bookstore ")
  
 def mark_book_unread(self,name):
   for book in self.books:
    if book['name']==name:
     book.unmark_book();
     save_to_file(repr(self),"book.txt")
     return;
   print (f"Book {name} not found in the bookstore ") 
     
 def add_book(self,book):
  if isinstance(book,Book):
   self.books.append(book);
   save_to_file(repr(self),"book.txt")
  else:
   print( f'the book you added is a {book.__class__.__name__}, not a book class')
 def delete_book(self,name):
   self.books=[book for book in self.books if book['name']!=name]
   save_to_file(repr(self),"book.txt")
   
 