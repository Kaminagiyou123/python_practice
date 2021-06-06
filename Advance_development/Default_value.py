accounts={
 'checking':1834,
 'saving':3342
 
}
def add_balance(account:float,name:str='checking')->float:
 accounts[name]+=account
 return accounts[name]

transactons=[
 (-190,'checking'),
 (3343,'saving'),
 (-190,'saving'),
]

for t in transactons:
 add_balance(*t)

for t in transactons:
 add_balance(account=t[0],name=t[1])
 
print(accounts["checking"])
print(accounts["saving"])

