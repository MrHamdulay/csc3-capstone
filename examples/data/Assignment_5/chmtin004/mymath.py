"""Module to use for Qu 3
Tinotenda Chevmura (CHMTIN004)
14 April 2014"""

def get_integer (var1):
   
   n = input ("Enter "+var1+":\n")
   while not n.isdigit ():
      n = input ("Enter "+var1+":\n")
   n = eval (n)   
   return n

def calc_factorial (var2):
   nfactorial = 1
   for i in range (1, var2+1):
      nfactorial *= i
   return nfactorial
