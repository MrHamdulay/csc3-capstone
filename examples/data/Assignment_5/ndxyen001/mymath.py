# Yentl Naidu (NDXYEN001)
# 17 April 2014
# Assignment 5
# Question 3

import math
def get_integer (x): 
   num=input("Enter "+x+":\n") 
   while not num.isdigit(): 
      num=input("Enter "+x+":\n")
   return eval(num) 
def calc_factorial (i): 
   fact= math.factorial(i) 
   return fact