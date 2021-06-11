from collections import deque
from types import coroutine

friends=deque(('Rolf',"Jose","Charlie","Jen","Anna"))

@coroutine
def friends_upper():
 while friends:
  friend=friends.popleft().upper()
  greeting=yield
  print(f'{greeting} {friend}')
  
async def greet(g):
  await g
  

greeter=greet(friends_upper())
greeter.send(None)
greeter.send("Hello")
greeting=input("Enter your greeting: ")
greeter.send(greeting)



