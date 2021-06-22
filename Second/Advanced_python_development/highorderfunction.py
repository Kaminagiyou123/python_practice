def greet():
 print('Hello')
 
def before_and_after(func):
 print('Before...')
 func()
 print('After...')

movies=[
 {'name':'1917','director':"Mendes"}
]

def find_movie(expected,finder):
 for movie in movies:
  if finder(movie)==expected:
   return movie
  
 
find_by=input('what property are we searching by? ')
looking_for=input(' What are you looking for? ')
movie=find_movie(looking_for,lambda movie:movie[find_by])
print(movie or 'no movies found')