#program to calculate n and k permutations
#omphemeste molusi
#17 april 2014


selection=""
n=0 
k=0
def get_integer(c):
   selection=c
   if c=="n": 
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
def calc_factorial(a):
   if a==n: 
      nfactorial = 1
      for i in range (1, a+1):
         nfactorial *= i
      return nfactorial 
   else: 
      nkfactorial = 1
      for i in range (1, a+1):
         nkfactorial *= i
      return nkfactorial 
