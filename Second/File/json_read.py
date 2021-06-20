import json

with open("Second/File/csv_json.txt","r") as file:
 data=list(json.load(file)['friends'])
 
 
cars=[
 {'make':'Ford','model':'Fiesta'},
 {'make':'Ford','model':'Focus'}
]
 
with open("Second/File/csv_json.txt","w") as file:
  json.dump(cars, file)