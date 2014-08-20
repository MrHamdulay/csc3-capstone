#Amitha Doodnath
#DDNAMI001
#14/04/2014
#Programme to draw text-based graphs of mathematical functions


import math

function = input("Enter a function f(x):\n")
x = 0
y = 0


for rows in range(10,-11,-1): 
     for col in range(-10,11,1):
          x=col
          roundfx = round(eval(function))
          if roundfx == rows: #checks if value of function exists in given range
               print("o", end="")
          if rows==0 and col==0 and not rows == roundfx: #checks for origin
               print("+", end="")
          if col == 0 and not rows == 0 and not rows == roundfx: #checks for vertical axis
               print("|", end="")
          if rows==0 and not col==0 and not rows == roundfx: #checks for horizontal axis
               print("-", end="")
          else:
               if not rows == 0 and not col == 0 and not rows == roundfx: #fills empty spaces in the graph
                    print(" ", end="")
     print()