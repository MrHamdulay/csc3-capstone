#adapt
#tntrob001
#14/4/2014

import question3

def get_integer (a):
   n = input ("Enter " +  a + ":\n")
   while not n.isdigit ():
      n = input ("Enter " +  a + ":\n")
   n = eval (n)
   return n


def calc_factorial (c):
   nfactorial = 1
   for i in range (1, c +1):
      nfactorial *= i
   return nfactorial

def calc_factorial (d):
   nkfactorial = 1
   for i in range (1, d+1):
      nkfactorial *= i
   return nkfactorial
