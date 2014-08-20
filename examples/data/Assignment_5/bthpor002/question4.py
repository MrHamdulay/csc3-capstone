#Assignment 5
#Question 4

import math
function= input("Enter a function f(x):\n")
x=0
y=0

for y in range (10,-11,-1):
    for i in range(-10,11):
        x=i
        answer= round(eval(function))
        if answer==y:
            print("o",end="")
        if y==0 and i!=0 and y!= answer:
            print("-", end="")
        if y==0 and i==0 and y!= answer:
            print("+",end="")
        if i==0 and y!=0 and y!= answer:
            print("|", end="")
            
        else:
            if y!=0:
                if x!=0:
                    if y!=answer:
                        print(" ",end="")
    print()
    
    