"""mymath.py Permutations
Author : Musa Xakaza
Student# : XKZMUS001
Date : 13/04/2014"""

def get_integer (char):
   c = input ("Enter "+char+":\n")
   while not c.isdigit():
      c = input ("Enter "+char+":\n")
   return eval(c)

def calc_factorial(x):
   xfactorial = 1
   for i in range (1, x+1):
      xfactorial *= i
   return xfactorial