"""Graph for inputted function
Keyoolin Padayachee
16 April 2014
"""
import math
function = input("Enter a function f(x):\n")
for y in range(10,-11,-1):
     for x in range(-10,11,1):
          fx = round(eval(function)) # Changes the function into one that can be used
          if y == fx : print("o",end="") # prints the graph
          # prints the axis
          elif y == 0 and x == 0: print("+",end="")
          elif x == 0 : print("|",end="")
          elif y == 0 : print("-",end="")
          else : print(" ",end="")
     print("")
          