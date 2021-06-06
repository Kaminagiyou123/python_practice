def hundred_numbers():
 nums=[]
 i=0
 while i<100:
  yield i
  i+=1
 return nums

g=hundred_numbers()
print(next(g))
print(next(g))
print(list(g))

# for n in range (2,20):
#  for x in range (2,n):
#   if n%x==0:
#    print("{} equals {}*{}".format(n,x,n//x) )
#    break;
#  else:
#    print('{} is a prime number.'.format(n))

def prime_generator(bound):
 for n in range (2,bound):
  for x in range (2,n):
   if n%x==0:
    break
 else:
  yield n

class FirsHundredGenerator: 
 def __init__(self):
  self.number=0;
 def __next__(self):
  if self.number<100:
   current=self.number;
   self.number+=1;
   return current
  else:
   raise StopIteration()
  
my_gen=FirsHundredGenerator()
print(next(my_gen))
print(next(my_gen))

class prime_generator:
 def __int__(self,stop):
  self.start=2
  self.stop=stop
 def __next__(self):
  for n in range(self.start,self.stop):
   for x in range(2,n):
    if n%x==0:break
   else:
    current=n;
    self.start=n+1;
    return current
  raise StopIteration()

class FirstHundredIterable:
 def __iter__(self):
  return FirsHundredGenerator()
 
# print(sum(FirstHundredIterable()))
# for i in FirstHundredIterable():
#  # print(i)
 
class AnotherIterable:
 def __init__(self):
  self.cars=["F","fefa"]
 def __len__(self):
  return len(self.cars)
 def __getitem__(self,i):
  return self.cars[i]
 
for car in AnotherIterable():
 print (car)
 
my_numbers=[x for x in [1,2,3,4,5]]
my_numbers_gen=(x for x in [1,2,3,4,5]) 

print(my_numbers)
print (next(my_numbers_gen))
print (next(my_numbers_gen))
print (next(my_numbers_gen))