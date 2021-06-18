def multiply(*args):
 total=1
 for arg in args:
  total=total*arg
 return total

def add (*args):
 total=0
 for arg in args:
  total+=arg
 return total

def apply(*args,operator):
 if operator=="*":
  return multiply(*args)
 elif operator=="+":
  return add(*args)
 else:
  return "no operator applied"
 
 
print(apply(1,2,3,4,operator="*"))

