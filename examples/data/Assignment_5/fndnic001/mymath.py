# calculate number of k-permutations of n items
# Nic Findlay
# 10 april 2014
def get_integer():
   n = input ("Enter n:\n")
   while not n.isdigit ():
      n = input ("Enter n:\n")
   n = eval (n)
   k = input ("Enter k:\n")
   while not k.isdigit ():
      k = input ("Enter k:\n")
   k = eval (k)
   return(n,k)

def calc_factorial(n,k):   
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   
   nkfactorial = 1
   for i in range (1, n-k+1):
      nkfactorial *= i
   return nfactorial//nkfactorial
   
