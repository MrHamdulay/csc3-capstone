'''Calculates the number of k-permutations of n items
Inga Ndyoki
16 April 2014'''

choice=""

n=0
k=0
def get_integer(c):
   choice=c
   if c=="n": #gets input for the value of n
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n 
   else: #gets input for the value of k
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k 
def calc_factorial(a):
   if a==n: #calculates factorial for n
      nfactorial = 1
      for i in range (1, a+1):
         nfactorial *= i
      return nfactorial #returns n factorial
   else: #calculates factorial for n-k
      nkfactorial = 1
      for i in range (1, a+1):
         nkfactorial *= i
      return nkfactorial 
   #returns n-k factorial and prints

