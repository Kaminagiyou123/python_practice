class student():
 def __init__(self,name,grades):
  self.name=name
  self.grades=grades
  

 def average(self):
  return sum(self.grades)/len(self.grades)
 
 
 class Person:
  def __init__(self,name,age):
   self.name=name
   self.age=age
  # def __str__(self):
  #  return (f"{self.name} is {self.age}")
  
  def __repr__ (self):
   return ('hello')
   
  
 class ClassTest:
  def instance_method(self):
   print(f'called instance_method of {self}')
  @classmethod
  def class_method(cls):
   print(f'called class method of {cls}')
  
  @staticmethod
  def static_method():
   print('Called static method')
 
 
 test=ClassTest()
 test.instance_method()
 ClassTest.class_method()
 ClassTest.static_method()