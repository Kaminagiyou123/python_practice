class FirstHundredGenerator:
 def __init__(self):
  self.number=0
 
 def __next__(self):
  if self.number<100:
   current=self.number
   self.number+=1
   return current
  else:
   raise StopIteration()
  
  # iterable
 def __iter__(self):
  return self



class FirstHundredIterable:
 # iterable2
 def __iter__(self):
  return FirstHundredGenerator()

class AnotherIterable:
 def __init__(self):
  self.cars=['Fiesta','Focus']
   # iterable3
 def __len__(self):
  return len(self.cars)
 def __getitem__(self,i):
  return self.cars[i]

print(AnotherIterable()[1])