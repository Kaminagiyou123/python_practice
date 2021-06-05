import sqlite3
from sqlite3.dbapi2 import Cursor
connection=sqlite3.connect('data.db')
Cursor.exectute("Your SQL is here")
connection.commit()
connection.close()