accounts={
 'checking':2985,
 'saving':3845
}

def add_balance(amount:float,name:str='checking')->float:
 accounts[name]+=amount
 return accounts[name]

add_balance(500)
print(accounts)