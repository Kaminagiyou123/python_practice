from collections import deque

friends=deque(("Rolf","Jose","Charle","Jen","Anna"))

def get_friend(): 
 yield from friends
 
def greet(g):
 while True:
  try:
   friend=next(g)
   yield f'hello {friend}'
  except StopIteration:
   pass
  
friends_generator= get_friend()
g=greet(friends_generator)

c=get_friend()
print(next(g))
print(next(g))