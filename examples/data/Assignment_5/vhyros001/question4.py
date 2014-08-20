"""Assignment 5 question 4 text based graph of a function
Ross van der Heyde VHYROS001
14 April 2013"""

import math

f = input("Enter a function f(x):\n")

for y in range (10,-11,-1): #rows / y values
     for x in range (-10,11):# columns/ x values   
          if y == round(eval(f)):
               print("o",end="")          
          elif y ==0 and x==0:
               print("+", end = "")
          elif y==0:
               print("-", end="")
          elif x ==0 :
               print("|",end="")
          else:
               print(" ",end="")
     print()# move to new line
    
    
#round(x, n) x rounded to n digits, rounding half to even. If n is omitted, it defaults to 0. 