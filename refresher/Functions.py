def hello():
 print("hello")


# def user_age_in_sec():
#  user_age=int (input("Input your age: "))
#  age_seconds=user_age*365*24*60*60
 
#  print(f"Your age is {age_seconds}")
 
# user_age_in_sec()

add=lambda x,y :x+y

def double(x):
 return x*2

sequence=[1,3,4,5]
double=map(lambda x:x*2,sequence)

print([x for x in double])