#print a graph
#chris betteridge
#17 April 2014

#get input
import math
fofx=input("Enter a function f(x):\n")
#print graph
for y in range(10,-11,-1):
    for x in range(-10,11):
        if y==round(eval(fofx),0):
            print("o",end="")
        elif y==0 and x==0:
            print("+",end="")
        elif y==0:
            print("-",end="")
        elif x==0:
            print("|",end="")
        else:
            print(" ",end="")
    print()