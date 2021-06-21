def hundred_numbers():
 nums=[]
 i=0
 while i<10:
  yield i
  i+=1
  
g=hundred_numbers()
print(next(g))
print(next(g))

print(list(g))