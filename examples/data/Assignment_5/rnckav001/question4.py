#ass.5 Q4 graph
#Kavir Ranchod rnckav001
#17/04/2014
import math
func=input("Enter a function f(x):\n")
for i in range(10,-11,-1):
    for j in range(-10,11):
        x=j
        y=round(eval(func))
        if y == i:
            print("o",end="")
        elif j == 0 and i == 0:
            print("+",end="")
        elif j == 0:
            print("|",end="")
        elif i == 0:
            print("-",end="")
        else:
            print(" ",end="")
    print()