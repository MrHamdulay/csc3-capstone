# Author : Rayaan Fakier FKRRAY001
# Date : 15 - 04 - 2014
# Program which implements the idea of adapting other modules


def get_integer(n_or_k):
   if n_or_k == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
   
   elif n_or_k == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k
   

def calc_factorial (x):
   nfactorial = 1
   for i in range (1, x+1):
      nfactorial *= i
   return nfactorial