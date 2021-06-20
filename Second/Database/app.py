from utils import database


USER_CHOICE="""
Enter:
-'a' to add a book
-'l' list all books
-'r' to mark a book as complete
-'d' to delete a book
-'q' to quit

Your choice:"""

class Book:
 def __init__(self,name,author):
     self.name=name
     self.author=author
     self.read=False   
 def markread(self):
  self.read=True
 def __str__(self):
  read_status="Y"
  if self.read==False:
   read_status='N'
  return f'Book {self.name} by {self.author} Read:{read_status}'
  
def add_book():
 name_input=input("Enter the name of the book: ")
 author_input=input("Enter the author of the book: ")
 for book in database.books:
  if book.name==name_input:
   print("the book is already in booklist")
   return
 database.books.append(Book(name_input,author_input))
                         
def list_books():
 for x in database.books:
  print(x)

def mark_read():
 name_input=input("Enter the name of the book you read: ")
 for book in database.books:
  if book.name==name_input:
   book.markread()

def delete_book():
 name_input=input("Enter the name of the book you want to delete: ")
 for book in database.books:
  if book.name==name_input:
   database.books.remove(book)
   

def menu():
 user_input=input(USER_CHOICE)
 while user_input!='q':
  if user_input=='a':
   add_book()
  elif user_input=='l':
   list_books()
  elif user_input=='r':
   mark_read()
  elif user_input=='d':
   delete_book()
  user_input=input(USER_CHOICE)
   
 
menu()