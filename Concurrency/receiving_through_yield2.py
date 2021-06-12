from collections import deque
friends=deque(("Rolf","Jose","Charle","Jen","Anna"))

def friend_upper():
 while friends:
  friend=friends.popleft().upper()
  greeting=yield
  print(f"{greeting} {friend}")


def greet(g):
  yield from g


greeter=greet(friend_upper())
greeter.send(None)
greeter.send("Hello")
greeter.send("How are you")

