def create_account(name:str,holder:str,account_holders=None):
 if not account_holders:
  account_holders=[]
 print(id(account_holders))
 account_holders.append(holder)
 
 return {
  'name':name,
  'main_account_holder':holder,
  'account_holder':account_holders
 }
a1=create_account('checking','Rolf')

a2=create_account("saving",'Jen')

print(a2)