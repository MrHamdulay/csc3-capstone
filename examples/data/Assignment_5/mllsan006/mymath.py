# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

def get_integer (s):
   if s == "n":
      n = input ("Enter n:\n")
   
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)   
   
      return(n)

   if s == "k":
      k = input ("Enter k:\n")
   
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
   
      return(k)

def calc_factorial (n):

   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i

   return(nfactorial)