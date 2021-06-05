import random
def play():
 userInput= input("r for rock, p for papter, s for scissors:" );
 computer=random.choice(['r','p','s'])
 
 if userInput==computer:
   return 'tie'
 if is_win(userInput,computer):
   return 'you won'

 return 'computer won'
 
def is_win(player,opponent):
 if (player=='r' and opponent=='p') or (player=="s" and opponent=='p') or(player =='p' and opponent=='r'): 
  return True;
  
while True: 
 print(play());
 
 