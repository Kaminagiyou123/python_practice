def starts_with_r(friend):
 return friend.startswith("R")

friends=['Rolf','Jose','Anna','Mary']

starts_with_r=filter(lambda x:x.startswith("R"),friends)
# print(list(starts_with_r))

another_starts_with_r=(f for f in friends if f.startswith('R'))
# print(list(another_starts_with_r))

def my_custom_filter(func,iterable):
 for i in iterable:
  if func(i):
   yield i
print(list(my_custom_filter(lambda x:x.startswith("R"),friends)))  
