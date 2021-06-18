users=[
 (0,"Bob","password"),
 (1,"Rolf","Bob234"),
 (2,"Jose","rqwfe4rf"),
 (3,"userName","feafq3f")
]

username_mapping={user[1]:user for user in users}

username_input=input("Enter your username: ")
password_input=input("Enter your password: ")

_,username,password=username_mapping[username_input]

if password==password_input:
 print("Your detials are correct")
else:
 print("Your password is wrong")
 