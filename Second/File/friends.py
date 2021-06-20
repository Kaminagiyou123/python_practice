friends_input=input("Input your 3 friends and use ',' to seperate:  ")
friends=set(friends_input.split(','))


with open('Second/File/people.txt','r') as file:
 ns=file.readlines()
 people_nearby= {n.rstrip() for n in ns}
 friends_nearby=people_nearby.intersection(friends)
 
 with open('Second/File/nearby_friends.txt','w') as target_file:
  for i in friends_nearby:
   target_file.write(f"{i}\n")
  
  
  
  