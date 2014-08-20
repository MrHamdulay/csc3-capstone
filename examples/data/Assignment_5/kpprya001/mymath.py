def get_integer(letter):
   if(letter == "n"):
      
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

def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i   
   return nfactorial
   
   
   
