"""graph plotter 
adam edelberg
15 april 2014"""

import math

function = input("Enter a function f(x):\n")


for y in range (10, -11, -1):
    for x in range (-10 , 11):
  
        
        roundfx = round(eval(function))
        
      
        if roundfx == y:
            print("o", end="")
        elif y==0 and x==0:
            print("+", end="")
        elif x == 0:
            print("|", end="")        
        elif y==0:
            print("-", end="")        
        else:
            print (" ",end="")               
            
    print()