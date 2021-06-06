def greet():
 print("hello")
 
def before_and_after(func):
 print('Before...')
 print(func())
 print('After...')
 
movies=[
 {"name":"The Matrix", "director":"wachowski"}
]
def find_movie(finder):
 for movie in movies:
  if finder(movie)==expected:
   return movie

find_by=input(" What property are we searching by? ")
looking_for=input("what are you looking for: ")

movie=find_movie(looking_for,lambda movie: movie[find_by])
