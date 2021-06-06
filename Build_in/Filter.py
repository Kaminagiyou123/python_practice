friends=['Rolf','Jose',"Mary","Randy","Anna"]

def start_with_r(friends):
 return friends.startswith("R")

start_with_r=filter(start_with_r,friends)
start_with_r=filter(lambda x:x.startwith("R"),friends)
another_start_with_r= (f for f in friends if f.startswith('R'))

# print(list(start_with_r))
# print(list(start_with_r))

friends_lower=map(lambda x:x.lower(),friends)
friends_lower=(f.lower() for f in friends )
print(next(friends_lower))

class User:
 def __init__(self,username,password):
  self.username=username
  self.password=password
@classmethod
def from_dict(cls,data):
 return cls(data['username'],data['password'])

users=[
 {'username':'rolf','password':"123"},
 {'username':'tecladosome','password':"333"},
]
users=[User.from_dic(user) for user in users]
user=map(User.from_dict,users)