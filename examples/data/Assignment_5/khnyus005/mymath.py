"""Permutation Calculator
Yusuf Khan
17 April 2014"""

def get_integer(q):
   z = input ("Enter "+q+":\n")
   while not z.isdigit():
      z = input("Enter "+q+":\n")
   z = eval(z)
   return z

def calc_factorial(w):
   x = 1
   for i in range (w+1):
      if i!=0:
          x*= i
   return x