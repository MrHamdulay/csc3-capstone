'''module to help calculate number of k-permutations of n items
bhavana harrilal, edited by Patrick Boroughs
10 april 2014'''

def get_integer(char):
   if char=='n':
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval(n)        
      return n
   elif char=='k':
      k = input("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval(k) 
      return k
      

def calc_factorial (n):
   
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i   
   return nfactorial
   
def calc_factorial (nk):
   nkfactorial = 1
   for i in range (1, nk+1):
      nkfactorial *= i 
   return nkfactorial

