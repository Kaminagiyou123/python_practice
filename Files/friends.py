friends=input('Enter three friend names seperated by commas: ');
friends_list=friends.split(",")

people=open("Files/people.txt",'r')
people_nearby=[ line.strip() for line in people.readlines()];
people.close();
print(set(people_nearby))
print(set(friends_list))

friends_nearby=set(friends_list).intersection(set(people_nearby))
print(friends_nearby)

nearby_friends_file=open("Files/nearby_friends.txt","w")

for friend in friends_nearby:
 print(f"writing {friend}")
 nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()