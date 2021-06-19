import functools
def make_secure(access_level):
 def decorator(func):
  @functools.wraps(func)
  def secure_function(*args,**kwargs):
   if user['access_level']=='admin':
    return func(*args,**kwargs)
   else:
    return "No admin access"
  return secure_function
 return decorator
 
@make_secure('admin')
def get_password(panel):
 if panel=="admin":
    return "1234"
 elif panel=="Billing":
    return "4566"

@make_secure('guest')
def get_admin_password():
    return "1234"


user={'username':"jose",'access_level':'guest'}

print(get_password("admin"))