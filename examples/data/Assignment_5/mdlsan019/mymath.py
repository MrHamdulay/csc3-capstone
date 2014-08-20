# mymath.py
# A Program that calculates the number of Permutations
# Sanele Mdlalose
# MDLSAN019
# 16-04-2014
# Assignment5,Question3

def get_integer (variable):
   if variable=="n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      return int (n) 
   

   else:
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      return int (k)   



def calc_factorial (var):
   nfactorial = 1
   for i in range (1, var+1):
      nfactorial*=i
      
   return nfactorial   
   
