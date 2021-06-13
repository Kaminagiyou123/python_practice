from database import Database
from admin import Admin

a = Admin('paco', 'perez', 2)
b = Admin('rolf', 'smith', 1)

a.save()
b.save()

print(Database.find(lambda x:x['username']=='rolf'))