def named(**kwargs):
 return kwargs
 


def print_nicely(**kwargs):
 print(named(**kwargs))
 for arg,value in named(**kwargs).items():
  print(f"{arg}:{value}")
 
print_nicely(name="Bob",age=23)

def named(*args):
 return args

print(named(3,22))


def both (*args,**kwargs):
 print(args)
 print(kwargs)
 
both (1,3,4,name="bob",age=23)