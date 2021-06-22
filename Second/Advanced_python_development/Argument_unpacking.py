accounts={
 'checking':2000,
 'saving':3000
}

def add_balance(amount:float,name:str='checking')->float:
 accounts[name]+=amount
 return accounts[name]

transactions=[
 (-180.67,'checking'),
 (300,'saving'),
]


 

class User:
 def __init__(self,username,password):
  self.username=username
  self.password=password
  

users=[
 {'username':'rolf','password':"123"},
 {'username':'Jose','password':"345"}
]


user_objects=[User(**data) for data in users]

print(user_objects)

users=[
 ('rolf',"123"),
 ('Jose',"345")
]

user_objects=[User(*data) for data in users]