class RuntimeErrorWithCode(Exception):
 """
 Exception raised when a speicifc error code is needed
"""
 def __init__(self,message,error_code):
  super().__init__(f'Error code {error_code}:{message}')
  self.error_code=error_code

  

err= RuntimeError("An error happened",500)

print(err.__doc__)