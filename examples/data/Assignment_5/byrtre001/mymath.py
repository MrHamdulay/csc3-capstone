# calculate number of k-permutations of n items
# Trevor Byaruhanga
# 15 april 2014
def get_integer(a):
   if a == 'n':
      
      n = input ("Enter n:\n")
      
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return(n)
   
   else:
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return(k)

def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return (nfactorial)
def calc_factorial(k):   
   nkfactorial = 1
   for i in range (1, k+1):
      nkfactorial *= i
   return (nkfactorial)
   
   print ("Number of permutations:", nfactorial // nkfactorial)



