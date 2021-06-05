class Car:
 def __init__(self,make,model):
  self.make=make
  self.model=model

class Garage:
 def __init__(self):
  self.cars=[]
 
 def __len__(self):
  return len(self.cars)
 
 def add_car(self,car):
   if isinstance(car,Car):
     self.cars.append(car)
   else: 
     raise (TypeError(f"You were trying to add a {car.__class__.__name__}. You need to add a Car class instead"))
 

ford=Garage()
fiesta=Car("Ford","Fiesta")

try: 
 ford.add_car(fiesta)
except TypeError:
  print("your car is not a car")
except ValueError:
  print("something else is going on")
finally:
  print (f"The garage right now has {len(ford)} cars")
  

  
