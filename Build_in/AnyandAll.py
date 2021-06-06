friends = [
  {
    'name': 'Rolf',
    'location': 'Washington, D.C.'
  },
  {
    'name': 'Anna',
    'location': 'San Francisco'
  },
  {
    'name': 'Charlie',
    'location': 'San Francisco'
  },
  {
    'name': 'Jose',
    'location': 'San Francisco'
  },
]

your_location=input('where is your location now ')
friends_nearby= [f for f in friends if f['location']== your_location]
if any (friends_nearby):
 print("You are not alone")

print(all[0,1,2,3,4])
