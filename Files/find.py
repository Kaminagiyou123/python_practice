from file_operation import save_to_file
def find_in(iterable,finder,expected):
 for i in iterable:
  if finder(i)==expected:
   return i
 raise NotFoundErr("not found")

class NotFoundErr():
 pass;
  