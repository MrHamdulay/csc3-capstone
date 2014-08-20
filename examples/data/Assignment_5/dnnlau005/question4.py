"""draw graph of a mathematical function
Lauren Denny
17 April 2014"""

import math

#get a function f(x)
f = input("Enter a function f(x):\n")

#displays axes going from -10 to 10 and graph 
for y in range(10,-11,-1):
    for x in range(-10,11,1):
        fx = eval(f)
        #graph represented by o's where y=rounded value of f(x)
        if round(fx)==y:      
            print("o",end="") 
        elif x==0 and y==0:
            print("+",end="") #+ for origin
        elif y==0:
            print("-",end="") #- for x-axis
        elif x==0:
            print("|",end="") #| for y-axis
        else:
            print(" ",end="")
    print()
    
