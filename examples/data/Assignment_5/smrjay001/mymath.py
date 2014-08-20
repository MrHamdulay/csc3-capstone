"""
functions for calculating the number of k-permutations of n items
Jayan Smart
17 April 2014
"""

from math import *

def get_integer(x):
   if x =='k':
      while True:
        integer = input("Enter k:\n")
        try:
            ineger = int(integer)
        except ValueError:  # gets thrown on any input except an integer value
            continue
        if int(integer) >0:
            return int(integer)
   if x == 'n':
      while True:
        integer = input("Enter n:\n")
        try:
            ineger = int(integer)
        except ValueError:  # gets thrown on any input except an integer value
            continue
        if int(integer) >0:
            return int(integer)

def calc_factorial(x):
   ans = factorial(x)
   return ans
