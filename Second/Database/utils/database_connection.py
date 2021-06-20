import sqlite3

class DatabaseConnection:
 def __init__(self):
  self.connection=None
 def __enter__(self):
  self.connection= sqlite3.connect('Second/Database/utils/data.db')
  return self.connection
 
 def __exit__(self,exc_type, exc_value, tb):
  if exc_type or exc_value or tb:
   self.connection.close()
  else:
   self.connection.commit()
   self.connection.close()