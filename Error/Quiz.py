def power_of_two():
 r=False;
 while (r==False):
  user_input= input("Please input a number: ")
  try:
   n=float(user_input)
   n_square=n**2
   print (f"the power of two returns {n_square}")
   r=True;
   return n_square
  except ValueError:
   print("Your input is not a number, please provide a number")
   
power_of_two()