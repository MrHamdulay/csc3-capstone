#Graph generator
#Aniq Hartle
#16-04-2014

import math

#take in function entered by user and make user friendly for program
fx = input("Enter a function f(x):\n")
fx = fx.replace("x", "j")

#making use of co-ordinate system plot points
for i in range(-10,11):
    for j in range(-10,11):
        if -i==round(eval(fx)):
            print("o",end="")        
        elif i==0 and j==0:
            print("+",end="")        
        elif i == 0:
            print("-",end="")               
        elif j==0:
            print("|",end="")
        else:
            print(" ",end="")
    print()