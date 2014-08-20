#TEVIN CHETTY
#15 APRIL 2014
#QUESTION 4

import math #for round

graph=input("Enter a function f(x): \n")
 
for y in range (10, -11, -1):
    for x in range (-10, 11, 1):#nested loop as for each y value x runs through every possible value
        coordinate=round(eval(graph))
        if coordinate==y:
            print("o", end="")
        
        else:
            
            if y==0 and x==0: #origin
                print("+", end="")
            elif x==0: #y-axis
                print("|", end="")
            elif y==0:#x-axis
                print("-", end="")
            else:
                print(" ", end="")
    print()
        