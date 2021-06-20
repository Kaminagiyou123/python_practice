
from .database_connection import DatabaseConnection

def create_book_table():
  with DatabaseConnection() as connection:
    cursor=connection.cursor()
    cursor.execute('CREATE TABLE books (name text primary key,author text,read boolean)')
   
  
def add_book(name,author):
  with DatabaseConnection() as connection:
      cursor=connection.cursor()
      cursor.execute('INSERT INTO books VALUES(?,?,False)',(name,author))
      
 

def get_all_books():
   with DatabaseConnection() as connection:
      cursor=connection.cursor()
      cursor.execute('SELECT * from books')
      books=[{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()]

      return books


def markread(name): 
  with DatabaseConnection() as connection:
      cursor=connection.cursor()
      cursor.execute('UPDATE books SET read=True WHERE name=?',(name,))
      
   
  
def delete_book(name):
  with DatabaseConnection() as connection:
      cursor=connection.cursor()
      cursor.execute('DELETE FROM books WHERE name=?',(name,))

