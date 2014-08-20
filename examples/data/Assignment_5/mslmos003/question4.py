#Rorisang Moseli
# 16 April 2014
#program to draw text based graph of a mathematical function
import math 

function = input("Enter a function f(x):\n")

x=0
y=0

for y in range(10,-11,-1):
    for j in range(-10,11,1):
        x=j
        answer = round(eval(function))
        if answer == y:
            print("o",end="")
        if y==0 and j!=0 and y!=answer:
            print("-", end="")
        if y==0 and j==0 and y!=answer:
            print("+", end="")
        if j==0 and y!=0 and y!= answer:
            print("|", end="")
            
        else:
            if y!=0:
                if j!=0:
                    if y!= answer:
                        print(" ", end="")


    print()
    