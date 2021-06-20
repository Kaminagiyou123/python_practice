from utils import database


USER_CHOICE="""
Enter:
-'a' to add a book
-'l' list all books
-'r' to mark a book as complete
-'d' to delete a book
-'q' to quit

Your choice:"""


  
def add_book():
 name_input=input("Enter the name of the book: ")
 author_input=input("Enter the author of the book: ")
 database.add_book(name_input,author_input)

                         
def list_books():
 books=database.get_all_books()
 for book in books:
   print(book)

def mark_read():
 name_input=input("Enter the name of the book you read: ")
 books=database.get_all_books()
 for book in books:
  if book['name']==name_input:
   database.markread(name_input)

def delete_book():
 name_input=input("Enter the name of the book you want to delete: ")
 database.delete_book(name_input)
   

def menu():
 user_input=input(USER_CHOICE)
 database.create_book_table()
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