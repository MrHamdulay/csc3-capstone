#Annie
#graph functions using python
#16 April 2014

import math
func=input("Enter a function f(x): \n")

for y in range (10,-11,-1):
    for x in range (-10,11):
        output=round(eval(func))
        
        if y == output:
            print("o",end= "")
        elif y == 0 and x == 0:
            print("+",end= "")
        elif x == 0: 
            print("|",end= "")
        elif y == 0:
            print("-",end= "")
        
        else:
            print(" ",end= "")
            
    
    print()
        