""" mymath
Adam Edelberg
15 April 2014"""


def get_integer(n):
   
   if ( n == "k"):
      n = input ("Enter k:\n")
      
      while not n.isdigit ():
          
         n = input ("Enter k:\n")      
   else:
      n = input ("Enter n:\n")
           
      while not n.isdigit ():
               
         n = input ("Enter n:\n")         
  
   n = eval (n)   
   return n

def calc_factorial (n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i   
   return nfactorial