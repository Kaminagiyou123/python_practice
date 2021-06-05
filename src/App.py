import sys
sys.path.insert(0, '../src')
from bookstore import Bookstore,Book

bookstore=Bookstore();

book1=Book("Peter Pan","abc");
book2=Book("Learning Python","ddd")

bookstore.add_book(book1)
bookstore.add_book(book2)
print(bookstore)