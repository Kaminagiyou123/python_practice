def divide (dividend,divisor):
 if divisor==0:
  raise ZeroDivisionError("divided by zero")
 
 return dividend/divisor

def calculator(*values,operator):
 return operator(*values)

result=calculator(20,4,operator=divide)


def search(sequence,expected,finder):
 for elem in sequence:
  if finder(elem)==expected:
   return elem
 raise RuntimeError(f"Couldnt find an element with {expected}")

friends=[
 {"name":"rolf",'age':34},
  {"name":"Adam",'age':32},
    {"name":"Anne",'age':27},
         ]

def get_friend_name(friend):
 return friend['name']

print(search(friends,"rolf",lambda friend:friend['name']))