class Book:
 TYPES=('hardcover','paperback')
 
 def __init__(self,name,book_type,weight):
  self.name=name
  self.book_type=book_type
  self.weight=weight
  
 def __repr__(self):
  return f"<{self.name},{self.book_type}, weighing {self.weight} "
 
 @classmethod
 def hardcover(cls,name,page_weight):
  return Book(name,Book.TYPES[0],page_weight)
  
book=Book.hardcover("Harry Potter", 1500)
light= Book.hardcover("Harry Potter",500)

print(book)
print(light)
 
 