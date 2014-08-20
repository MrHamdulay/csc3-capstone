
import math

function = input("Enter a function f(x):\n")

for row in range(10,-11,-1):
     for col in range(-10,11):
          
          x = col
          y = row
          equation = eval(function)
          equation= round(equation)
          #print(equation)
          if equation == y:
               print("o",end='')          
          elif y == 0 and x == 0:
               print("+",end='')          
          elif x == 0:
               print("|",end='')
          elif y == 0:
               print("-",end='')          
          
          else: print(" ",end="")
               
          
     
     print()
        
    

