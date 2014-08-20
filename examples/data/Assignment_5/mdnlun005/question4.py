"""Lungelo Mdunge
Assignment 5 Question4"""

import math 
x=0
function=input("Enter a function f(x):"'\n')
 
for y in range (10,-11,-1):
      for x in range (-10, 11):
            function_1=eval(function)
            y_real = -y/10
            if x == 0 and y == round(function_1):
                  print ("o",end="")
            elif y == 0 and y == round(function_1):
                  print("o", end="")  
                   
            elif round(function_1) == y:
                  print("o",end="")
            
            elif x==0 and y==0:
                  print("+", end="")
            elif x==0:
                  print("|",end="")
            elif y==0:
                  print("-", end="")
            else:
                  print (" ",end="")   
      print ()
     