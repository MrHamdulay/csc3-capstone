
def get_integer(a):
   if a == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
   elif a == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

def calc_factorial(b):
   
   nfactorial = 1
   for i in range (1, b+1):
      nfactorial *= i
   return nfactorial
   
def calc_factorial(c):
   nkfactorial = 1
   for i in range (1, c+1):
      nkfactorial *= i
   return nkfactorial






   
  

#print ("Number of permutations:", nfactorial // nkfactorial)
