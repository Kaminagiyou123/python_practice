def divide(dividend,divisor):
 if divisor==0:
  raise ZeroDivisionError("Divisor cannot be 0")
  return
 
 return dividend/divisor


grades=[]

try: 
 average=divide(sum(grades)/len(grades))
 print(f"The average grade is {average}")
 
except ZeroDivisionError:
 print("There are no grades in your list")
 
