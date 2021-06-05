import json
with open("Files/friends_json.txt",'r') as file:
 file_contents=json.load(file)

print(file_contents['friends'][0])

# 
cars={"cars":[
 {"make":"ford",
  "model":"Fiesta"},
  {"make":"ford",
  "model":"Focus"}
]
}

with open("Files/json_file.txt",'w') as file:
 json.dump(cars,file)

# 
my_json_string='[{"name":"Alfa Romeo","realesed":1950}]'

incorrect_car=json.loads(my_json_string)
print(incorrect_car[0]["name"])