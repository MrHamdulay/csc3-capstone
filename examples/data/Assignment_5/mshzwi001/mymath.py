# calculate number of k-permutations of n items
# Mashau zwivhuya
# 14 april 2014

def get_integer (option):
   number=0
   if option=="n":
      n = input ("Enter n:\n")
      while n.isdigit()==False:
         n = input ("Enter n:\n")
      n = eval (n)
      number=n
   elif option=="k":
      k = input ("Enter k:\n")
      while k.isdigit()==False:
         k = input ("Enter k:\n")
      k = eval (k)
      number=k
   return number

def calc_factorial(integer):
   nfactorial = 1
   for i in range (1, integer+1):
      nfactorial *= i   
   return nfactorial
         






