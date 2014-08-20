# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

n = ""
k = ""
o = 0
l = 0
def get_integer(z):
   global n
   global k
   global o
   global l
   if z == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      o = eval (n)  
      
      
   elif z == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      l = eval (k)
      
      return o, l
      

o = o
l = l
nfactorial = 1
nkfactorial = 1
def calc_factorial(x):
   global n
   global k
   global nfactorial
   global nkfactorial
   
   if x == n:
      nfactorial = 1
      n = eval(o)
      for i in range (1, n+1):
         nfactorial *= i
   
   elif x == n-k:      
      nkfactorial = 1
      k = eval(l)
      for i in range (1, n-k+1):
         nkfactorial *= i
         
   return nfactorial, nkfactorial

#print ("Number of permutations:", nfactorial // nkfactorial)
