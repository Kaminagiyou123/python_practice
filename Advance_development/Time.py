import time

def measure_runtime(func):
 start=time.time()
 func()
 end=time.time()
 return end-start
 

def power(limit):
 return [x**2 for x in range (limit)]

print(measure_runtime(lambda:power(5000)))

import timeit
print(timeit.timeit("[x**2 for x in range (10)]"))
