"""
Permutations
Genevieve Brownyn Chetty (CHTGEN002)
16/04/2014
"""
def get_integer(x):
  
  if(x=='n'):
    n=input("Enter n:\n")
    while not n.isdigit(): #if n is a string, convert to integer
      n=input("Enter n:\n")
    n=eval (n)
    return n #returns as integer
  
  elif(x=='k'):
    k=input("Enter k:\n")
    while not k.isdigit(): #if k is string
      k=input("Enter k:\n")
    k=eval(k)
    return k #returns as integer
  
def calc_factorial(y): #return factorial
  factorial=1
  for i in range (1, y+1):
    factorial *= i
  return factorial