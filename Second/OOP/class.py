class my_student:
 def __init__(self,name:str,grades:list[int]):
  self.name=name
  self.grades=grades
 @property 
 def average(self):
  try:
   average=sum(self.grades)/len(self.grades)
   return average
  except ZeroDivisionError:
   pass
   return f"{self.name} doesnt have grade documented yet"
 def __str__(self):
  return f"Student {self.name}, scores: {self.grades} "
 
 # need these two below to run for loop
 def __len__(self):
  return len(self.grades)
 def __getitem__(self,i):
  return self.grades[i]
 
 
class paid_student(my_student):
 def __init__(self,name,grades,salary):
  super().__init__(name,grades)
  self.salary=salary
 def __str__(self):
  return f"Student {self.name}, scores: {self.grades}, hourly salary is ${self.salary} "
 @property
 def weekly_salary(self):
  return self.salary*37.5
   

class Student:
 def __init__(self,name,school):
  self.name=name
  self.school=school
  self.marks=[]
 def average(self):
  return sum(self.marks)/len(self.marks)
 
rolf=Student("Rolf","MIT")
rolf.marks.append(78)
rolf.marks.append(89)
print(rolf.average())

class Foo:
 @classmethod
 def hi(cls):
  print(cls.__name__)
  
class Bar:
 @staticmethod
 def hi():
  print("hello")



class FixedFloat:
 def __init__(self,amount):
  self.amount=amount
 def __repr__(self):
  return f'<fixedFloat {self.amount:.2f}>'
 @classmethod
 def from_sum(cls,value1,value2):
  return cls(value1+value2)

class Euro(FixedFloat):
 def __init__(self,amount):
  super().__init__(amount)
  self.symbol='e'
 
 def __repf__(self):
  return f"<Euro {self.symbol}{self.amount:.2f}>"
  
money=Euro.from_sum(14.32423,234234234.2342)
 
print(money)
  