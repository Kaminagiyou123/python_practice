from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
 def walk(self):
  print('walking...')
 @abstractmethod
 def num_legs(self):
  pass

class Dog(Animal):
 def __init__(self,name):
  self.name=name
 def num_legs(self):
  return 4
 
class Monkey(Animal):
  def __init__(self,name):
   self.name=name
  def num_legs(self):
   return 2

animals=[Dog('Rolf'),Monkey('Rob')]

for a in animals:
 print(a.num_legs())