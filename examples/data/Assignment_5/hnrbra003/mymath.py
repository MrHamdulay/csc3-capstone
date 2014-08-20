"""My math module for question 3
Brandon Hinrichsen 
16/04/2014"""

def get_integer(num):
   if num == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n") 
      n = eval(n)
      return n
   
   if num == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

      
def calc_factorial(integer):   
   nfactorial = 1
   for i in range (1, integer+1):
      nfactorial *= i
   return nfactorial  