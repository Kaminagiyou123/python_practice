import time
from concurrent.futures import ProcessPoolExecutor

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


if __name__ == '__main__':
 start=time.time()
 with ProcessPoolExecutor(max_workers=2) as pool:
   pool.submit(complex_calculation)
   pool.submit(complex_calculation)

 print(f'Two process total time: {time.time()-start}')
