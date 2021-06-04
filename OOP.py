
class Student:
 def __init__(self,new_name,new_grades):
  self.name=new_name;
  self.grades= new_grades;
 def average(self):
  return sum(self.grades)/len(self.grades)
 
student_one=Student("Rob",[22,32,1,222])
# print(student_one.average());

class Movie:
 def __init__(self,name,director):
  self.name=name;
  self.director=director;
 
 def print_info(self):
  print (" The movie is "+self.name +" and director is "+self.director)

class Garage: 
 def __init__(self) :
     self.cars=[]
 def __len__(self):
  return len(self.cars);
 def __getitem__(self,i):
  return self.cars[i]
 def len(self):
  return len(self.cars) 
 def __repr__(self):
  return f'<Garage {self.cars}>'
 def __str__(self):
  return f'Garage with {len(self)} cars'
  
G1=Garage();
G1.cars.append("Ford");
G1.cars.append("Focus");


class Club:
 def __init__(self,name)  :
  self.name=name
  self.players=[]
 def __getitem__(self,i):
  return self.players[i]
  
 def __repr__(self) :
     return f"Club {self.name}: {self.players}";
 def __str__(self):
  return f"Club {self.name} has {len(self.players)} players"
 
my_club= Club("Arsenal")
my_club.players.append("Rolf")
my_club.players.append("Anne")


class Student:
 def __init__(self,name,school) :
  self.name=name;
  self.school=school;
  self.marks=[]
  
 def average(self):
  return sum(self.marks)/len(self.marks)
 
class WorkingStudent(Student):
 def __init__(self,name,school,salary):
  super();
  self.salary=salary;
  
 @property
 def weekly_salary(self):
  return self.salary*37.5
 
class FixedFloat:
 def __init__(self,amount) :
     self.amount=amount;
     
 def __repr__(self) :
  return f'<Fixed Float {self.amount:.2f}>'
 
 @classmethod
 def from_sum(cls,value1, value2):
  return cls(value1+value2)
 
class Euro(FixedFloat):
 def __init__(self,amount):
   super().__init__(amount);
   self.symbol='e'
  
 def __repr__(self):
  return f'<Euro {self.symbol}{self.amount:.2f}>'
 

num= Euro.from_sum(34.232,32342.33)
print(num)

 
 

