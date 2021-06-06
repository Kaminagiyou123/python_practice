# friends_last_seen={
#  "Rolf":21,
#  "Jen":1,
#  "Anne":1
# }

# def see_friend(friends,name):
#  print(id(friends))
#  friends[name]=0
 
# print(id(friends_last_seen))
# print(id(friends_last_seen['Rolf']))
# see_friend(friends_last_seen,"Rolf")
# # print(id(friends_last_seen))
# print(id(friends_last_seen['Rolf']))


# age=20
# def increase_age(current_age):
#  print(id(current_age))
#  current_age=current_age+1
#  print(id(current_age))
 
 
# print(id(age))
# increase_age(age)
# print(id(age))

primes=[2,3,5]
print(id(primes))
primes+=[2,3,5,7,11]
print(id(primes))
print("++++++")
primes=[2,3,5]
print(id(primes))
primes=primes+[7,11]
print(primes)
print(id(primes))
print("++++++")

primes=2
print(id(primes))
primes+=3
print(id(primes))
