# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

#modified by Roger Cox
def get_integer (a):
   # If loop to differentiate between n and k
   if (a=="n"):
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n) 
      return n


   else:
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k
   
# this function will be called twice
def calc_factorial(n):
   
      nfactorial = 1
      for i in range (1, n+1):
         nfactorial *= i
      return nfactorial
  
  
  
