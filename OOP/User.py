class User:
 def __init__(self,name,engagement) :
     self.name=name;
     self.engagement=engagement;
 def __repr__(self) :
     return f'<User {self.name}>'
    
    
def get_user_score(user):
 try:
   perform_calculation(user.engagement)  
 except KeyError:
  print("Incorrect values provided to our calculation function")
 else:
  print( perform_calculation(user.engagement)  )
  if (perform_calculation(user.engagement)  >500):
    send_notification(user)

def perform_calculation(metrics):
 return metrics['clicks']*5+metrics["hits"]*2
 
def send_notification(user):
 print(f'Notification sent to {user}')


my_user=User('Rolf',{'clicks':151,'hits':399})
# my_user=User("Rosie",{'click':151})

get_user_score(my_user)