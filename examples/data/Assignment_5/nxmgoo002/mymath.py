""" This programm calculates the k-permutations
Nxumalo Goodman
18 April 2014"""

def get_integer(n):
   b = ""
   
   while not b.isdigit ():
      b = input ('Enter '+n+':\n')
   return int(b)
      
def calc_factorial(a):
   nfactorial = 1
   
   for i in range (1,a + 1):
      nfactorial *= i 
      
   return nfactorial
   
