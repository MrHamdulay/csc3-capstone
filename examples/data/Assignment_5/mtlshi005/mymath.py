
def get_integer(a):
   if a=="n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
   
   if a=="k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

def calc_factorial(n):
      
      nfactorial = 1
      for i in range (1, (n)+1):
         nfactorial *= i
      return nfactorial       
      
   #if x==(n-k):
    #  nkfactorial = 1
    #  a=nkfactorial
     # for i in range (1, n-k+1):
      #   nkfactorial *= i
      #return nkfactorial

