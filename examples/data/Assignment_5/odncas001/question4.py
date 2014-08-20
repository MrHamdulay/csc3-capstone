"""program for graphically representing basic generic functions
casey o'donnell
15 april 2014"""

import math
fx=input("Enter a function f(x):\n")
for y in range(-10,11):
    for x in range(-10,11):
        real_y=-y
        ans=eval(fx)
        ans=round(ans)
        if ans==real_y:
            print("o",end="")
        elif x==0 and real_y==0:
            print("+",end="")
        elif x==0:
            print("|",end="")
        elif real_y==0:
            print("-",end="")
        else:
            print(" ",end="")
    print()
        
    
    
    
