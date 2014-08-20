#Thea Sitek

import math
    
expression = input("Enter a function f(x):\n")
x = 0
    
#    fx = ['']*21  
#    i=0
#    for x in range(-10,11,1):
#        fx[i] = int(round(eval(expression)))
#        i +=1   



for row in range(10,-11,-1):   #y values
   for col in range(-10,11,1):   #x values
      x = col
      fx = round(eval(expression))   #calgulate f(x) for each x
      if fx == row:
          print("o", end="")
      elif row==0 and col==0:
          print("+", end="")
      elif col == 0:
          print("|", end="")
      elif row==0:
          print("-", end="")
      else:
          print(" ", end="")      
   
   print()