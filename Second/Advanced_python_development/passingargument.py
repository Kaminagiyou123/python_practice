friends_last_seen={
 "Rolf":31,
 "Jen":1,
 "Anne":7
}
def see_friend(friends,name):
  print(id(friends))
  friends[name]=0

age=20

def increase_age(current_age):
 current_age+=1
 return current_age

print(id(age))
print(id(increase_age(age)))

primes=[2,3,5]

primes=primes+[7,11]
