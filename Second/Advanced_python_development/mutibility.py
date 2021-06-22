"""
Integer,string,float,tuple Immutable
"""

friends_last_seen={
 'Rolf':31,
 'Jen':1,
 'Anne':7
}
another_variable=friends_last_seen

my_int=5
my_int+=1

friends=['Rolf','Jose']
friends.append('Anne')

print(id(friends[0]))
friends[0]='Bob'
print(id(friends[0]))