number=7


while True:
  user_input=input("Enter 'y' if you want to play:(Y/n) ").lower()
  if user_input=='n':
   break
  user_number=int(input("Guess our number: "))
  if user_number==number:
   print("You guessed correctly")
  elif abs(user_number-number)==1:
   print("You are off by one")
  else:
   print("Sorry it is not correct")
 
