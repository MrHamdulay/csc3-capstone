#Thembekile Dubazana
#dbzphi002
#Assignment 2:Q4
#April 2014

import math
#User must enter the function
function = input("Enter a function f(x):\n")

#Find the values/coordinates of x and y
for y in range(10,-11,-1):
        for x in range(-10,11,1):
                value=round(eval(function))
                if value==y:
                        print("o",end="")
                if x==0 and y==0 and not value==y:
                        print("+",end="")
                if x==0 and not y==0 and not y ==value:
                        print("|",end="")
                if y==0 and not x==0 and not y==value:
                        print("-",end="")
                else:
                        if not y==0:
                                if not x==0:
                                        if not y==value:
                                                print(" ",end="")
        print()
                                                
                        
                        
                
                
        
        