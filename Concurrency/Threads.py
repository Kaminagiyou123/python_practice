import time

from concurrent.futures import ThreadPoolExecutor

def ask_user():
 user_input=input("Enter your name: ")
 great=f"Hello,{user_input}"
 print(great)
 
def complex_calculation():
 print("start calculating...")
 [x**2 for x in range (20000000)]
  

start=time.time()  
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time()-start}')



start=time.time() 
with ThreadPoolExecutor(max_workers=2) as pool:
 pool.submit(complex_calculation)
 pool.submit(ask_user)

print(f'Single thread total time: {time.time()-start}')