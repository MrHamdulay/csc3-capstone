"""Saijil Nemchund
Question 1 
16 April 2014"""

#Programme to draw text-based graphs of mathematical functions


import math

function = input("Enter a function f(x):\n")
x = 0
y = 0


for rows in range(10,-11,-1): 
     for col in range(-10,11,1):
          x=col
          roundfx = round(eval(function))
          if roundfx == rows: #ensures that function exists in the range available
               print("o", end="")
          if rows==0 and col==0 and not rows == roundfx: #origin
               print("+", end="")
          if col == 0 and not rows == 0 and not rows == roundfx: #Vertical axis
               print("|", end="")
          if rows==0 and not col==0 and not rows == roundfx: #Horizontal axis
               print("-", end="")
          else:
               if not rows == 0 and not col == 0 and not rows == roundfx: #This fills spaces that are empty
                    print(" ", end="")
                    
                    
                    
     print()