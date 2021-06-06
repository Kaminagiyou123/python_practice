# counter
from collections import Counter, defaultdict, namedtuple,deque

device_temperatures=[12.4,55,232,33,2.1,2.1]
temperature_counter= Counter(device_temperatures)

# print(temperature_counter[2.1])

# default_dic

coworkers=[('Rolf','MIT'),("Jen","Oxford"),('Rolf','Cambridge')]

alma_maters=defaultdict(list)
alma_maters.default_factory=None;
# for coworker,place in coworkers:
#  alma_maters[coworker].append(place)

my_company='Teclado'
coworkers=['Jen',"Li","Charlie"]
other_coworkers=[('Rolf',"Apple Inc"),("Anna","Google")]

coworker_companies=defaultdict(lambda:my_company)

for person,company in other_coworkers:
 coworker_companies[person]=company
 
# print(coworker_companies)

#nametuple
Account=namedtuple("Account",['name','balance'])
account=Account('checking',18293)

#deque
friends=deque(['Rolf',"Charlie","Jen","Anna"])
friends.append("Jose")
friends.appendleft("Anthony")

friends.popleft()
friends.pop()

print(friends)