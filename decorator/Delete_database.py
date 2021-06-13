user={
 'id':1,
 'name':"Jose",
 "role":"guest"
}

def delete_database():
 print('Database deleted')
 
def check_permission(func):
 def wrapper():
  if user.get('role')=='admin':
   return func()
  else:
   raise PermissionError("You are not an admin")
 return wrapper

secure_delete_database=check_permission(delete_database)