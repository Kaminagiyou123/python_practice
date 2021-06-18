name="Bob"
greeting=f'Hello {name}'

# print(greeting)
name="Rolf"
greeting=f'Hello {name}'
# print(greeting)

name="RR"
greeting="Hello,{}"
with_name=greeting.format(name)
# print(with_name)

longer_phrase="Hello,{},today is {}"
formated=longer_phrase.format("rolf",'TUESDAY')
# print(formated)

# name=input("enter you name: ")
# size=input("enter the size of your house: ")
# square_meters=float(size)/10.8
# print(f"hello {name}, the size of your house is {square_meters:.2f}")

# l=['bob','rolf','Anne']
# t=('Bob',"Rolf","Anne")
# s={"Bob","Rolf","Anne"}
# l.append("Smith")
# s.add("Smith")
# print(s)

friends={"Bob","Rolf","Anne"}
abroad={"Bob","Anne"}
local_friends=friends.difference(abroad)
friends=local_friends.union(abroad)

art={'Bob','Jen','Rolf','Charlie'}
science={'Bob','Jen','Adam','Anne'}

# both=art.intersection(science)

# day_of_week=input(" What day of the week is today: ").lower()

# if day_of_week=="monday":
#    print("today is Monday") 
# else:
#    print("today is not Monday")
   
movies_watched=['The Matrix','Green Book',"Her"]
user_movie=input("Enter something you've wathced recently: ")
if user_movie in movies_watched:
 print(user_movie)
