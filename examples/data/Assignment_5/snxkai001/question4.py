#kairav soni graphs

import math

equation=input("Enter a function f(x):\n")


yinc=0.49

for yval in range(10,-11,-1):
    
    
    for x in range(-10,11):
        
        
        if (yval-yinc)<=eval(equation)<=(yval+yinc):
                print("o",end="")
                
            
            
        else:
            
            if x==0 and yval==0:
                print("+",end="")
                
            
            elif yval==0:
                print("-",end="")
                
                
            elif x==0:
                print("|",end="")
                
                
            else:
                print(" ",end="")
                
    print()
        
        