friends=['Rolf','Jose','Anna','Mary']

starts_with_r=filter(lambda x:x.startswith("R"),friends)
# print(list(starts_with_r))

another_starts_with_r=(f for f in friends if f.startswith('R'))

friends_lower=map(lambda x:x.lower(),friends)
print(starts_with_r)

class User:
 def __init__(self,username,password):
  self.username=username
  self.password=password
  
 @classmethod
 def from_dict(cls,data):
  return cls(data['username'],data['password'])
 
users=[
  {'username':'rolf','password':'123'},
  {'username':'Rosie','password':'RosieRo'}
 ]
users=map(User.from_dict,users)
print(users)

