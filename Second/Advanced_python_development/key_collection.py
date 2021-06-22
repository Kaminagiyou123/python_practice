from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque


device_temperatures=[13.4,55,323,2,33,16,5,5,5]
temperature_counter=Counter(device_temperatures)
print(temperature_counter)


my_dict={'hello':5}
coworkers=[('Rolf',"MIT"),("Jen","Oxford")]
alma_maters=defaultdict(list)
for coworker,place in coworkers:
  alma_maters[coworker].append(place)

my_company='Teclado'

coworkers=['Jen','LI',"Charlie",'Rhys']
other_coworkers=[('Rolf',"Apple inc"),('Anna','Google')]
coworker_companies=defaultdict(lambda:my_company)
for person,company in other_coworkers:
 coworker_companies[person]=company
 
account=("checking",1892)
Account=namedtuple('Account',['name','balance'])
account=Account(name='checking',balance=1892)

friends=deque(('Rolf','Charlie','Jen','Anna'))
friends.popleft()
print(friends)