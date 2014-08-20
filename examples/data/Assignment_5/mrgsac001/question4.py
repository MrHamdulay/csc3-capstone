

"""Graph
Sachin Murugan 
17/04/2014"""
import math 

graph=input("Enter a function f(x): \n")
 #create a nested loop to run through each y and x value
for y in range (10, -11, -1):
    for x in range (-10, 11, 1):
        coordinate=round(eval(graph))
        if coordinate==y:
            print("o", end="")
        
        else:
            #create origin, y values and x values
            if y==0 and x==0: 
                print("+", end="")
            elif x==0: 
                print("|", end="")
            elif y==0:
                print("-", end="")
            else:
                print(" ", end="")
    print()
        