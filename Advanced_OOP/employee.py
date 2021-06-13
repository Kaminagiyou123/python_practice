
class Salary:
    # define Salary class and associated methods here
    def calculate(self,hours):
      return hours*self.rate


class Promotable:
    # define Promotable class and associated methods here
    def promote(self,increase):
     self.rate= self.rate+increase


# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)
       
       
rolf=Employee(15.0)
print(rolf.weekly_salary())

rolf.promote(5)
print(rolf.weekly_salary())