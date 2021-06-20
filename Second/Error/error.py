class Car:
 def __init__(self,make,model) -> None:
     self.make=make
     self.model=model
 def __repr__(self):
  return f"{self.make} {self.model}"

class Garage:
 def __init__(self) -> None:
     self.cars=[]   
 def __len__(self):
     return len(self.cars)
 def add_car(self,car):
  if not isinstance(car,Car):
   raise TypeError(f"Tried to add a {car.__class__.__name__} to garage")
  self.cars.append(car)

ford=Garage()
car = Car('Ford','Fiesta')
try:
    ford.add_car(car)
except TypeError:
    print("Your car was not a car")
finally:
    print(f'Your garage current has {len(ford)} cars')

  
  