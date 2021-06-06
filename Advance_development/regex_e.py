import re
def is_filename_safe(name:str):
 expression="^[a-zA-Z0-9]+[-_()][\.jpg|\.jpeg|\.png|\.gif]"
 
 return re.match(expression,name) is not None

print(is_filename_safe("ttt_.jpg"))