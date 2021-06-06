def create_account(name:str,holder:str,account_holders:list=None):
 # use non-mutible variables in default arguments
 if not account_holders:
  account_holders=[]
 print(id(account_holders))
 account_holders.append(holder)
 
 return {
  'name':name,
  'main_account_holder':holder,
  "account_holders":account_holders
 }
 
a1=create_account("checking","Rolf")
a2=create_account("saving","Jen")
print(a1)
print(a2)