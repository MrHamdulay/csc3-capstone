# calculate number of k-permutations of n items
# Shaun Muzenda
# 14 April 2014

def get_integer(st):
   if st == "n":
      n = input ("Enter n:\n")         #inputing the value of the base
      while not n.isdigit ():          #if n entered is not a number, keep asking for a number till one is entered
         n = input ("Enter n:\n")
      n = eval(n)             
      return n
   
   if st == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():          #if k entered is not a number, keep asking for a number till one is entered
         k = input ("Enter k:\n")
      k = eval (k)
      return k

      
def calc_factorial(integer):   
   nfactorial = 1
   for i in range (1, integer+1):
      nfactorial *= i
   return nfactorial  