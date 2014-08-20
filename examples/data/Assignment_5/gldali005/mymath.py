# program that consists of functions that calculates the number of k-permutations of n items
# Ali Goldstein
# 16 April 2014

#function that return integers
def get_integer(n):
  if n== "n":
    n = input ("Enter n:\n")
    while not n.isdigit ():
        n = input ("Enter n:\n")
    n = eval (n) 
    return n
  elif n=="k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
          k = input ("Enter k:\n")
      k = eval (k) 
      return k
    
#function that returns factorial of integers           
def calc_factorial (n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
       
