import functools

user={'username':"Jose123","access_level":"admin"}

def third_level(access_level):
 def user_has_permission(func):
  @functools.wraps(func)
  def wrapper(*args,**kwargs):
   if user.get('access_level')==access_level:
    return func(*args,*kwargs)
  return wrapper
 return user_has_permission

@third_level('admin')
def my_function(panel):
 return f"Password for  {panel} is 1234"

@third_level('admin')
def other_function():
  pass
print(my_function("movies"))
print(other_function())