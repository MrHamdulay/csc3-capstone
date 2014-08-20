''' program to calculate k permutations of n terms
 Mokoena Mafologele
 16/04/2014'''
choice=""
#get global values
n=0 
k=0
def get_integer(c):
   choice=c
   #get the value of n as an evaluated value
   if c=="n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      #returns the evaluated 
      return n
   else:
      #get input of k
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
         #evaluate k
      k = eval (k)
      return k #returns k
def calc_factorial(a):
   if a==n: #caters for choice
      nfactorial = 1
      #calculate factorial
      for i in range (1, a+1):
         nfactorial *= i
      return nfactorial #returns n as a function of the factorial
   else: #calculates the factorial of n-k
      nkfactorial = 1
      for i in range (1, a+1):
         nkfactorial *= i
      return nkfactorial #stores n-k
#print ("Number of permutations:", nfactorial // nkfactorial)
