csv_file=open("Files/csv_data.txt",'r');
lines=csv_file.readlines();
csv_file.close();

lines=[line.strip() for line in lines[1:]];

for line in lines:
 person_data=line.split(",");
 name=person_data[0].title();
 age=person_data[1].capitalize();
 univeristy=person_data[2].capitalize();
 degree=person_data[3].capitalize();
 
 print(f'{name} is {age}, studying {degree} at {univeristy}')
 
 sample_csv_value=(",").join(['Rose','25','MIT',"CS"])
 print(sample_csv_value)
 