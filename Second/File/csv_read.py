with open('Second/File/csv_data.txt','r') as file:
 lines=file.readlines()
 
lines=[line.strip() for line in lines[1:]]
for line in lines:
 personal_data=line.split(",")
 name=personal_data[0]
 age=personal_data[1]
 univeristy=personal_data[2]
 degree=personal_data[3]
 print (f'{name.title()} is {age}, studying {degree.capitalize()} in {univeristy.capitalize()}')
 