# Question 3- Assignment 5
# Duncan Saffy
# 15-04-2014

def get_integer (n):
   if n=="n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)   
      return n
   if n=="k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k=eval(k)
      return k
    

def calc_factorial (c):
   nfactorial = 1
   for i in range (1, c+1):
      nfactorial *= i
   return nfactorial
