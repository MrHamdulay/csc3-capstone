#Module mymath

import math

def get_integer(var):
   string = "Enter " + var + ":\n"
   num = input (string)
   while not num.isdigit ():
      num = input (string)
   ans = eval(num)
   return ans

def calc_factorial(n):
   out = math.factorial(n)
   return out