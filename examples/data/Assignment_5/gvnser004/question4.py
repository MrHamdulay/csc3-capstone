"""Serayen Govender
16 April 2014
question 4"""

import math

def main():
    f = input("Enter a function f(x):\n")
    
    for i in range(10,-11,-1):
        for j in range(-10,11,1):
            x=j
            roundf = round(eval(f))
            if roundf == i:
                print("o", end="")
            elif i==0 and j==0:
                print("+", end="")
            elif j == 0 and i != 0:
                print("|", end="")
            elif i==0 and j!=0:
                print("-", end="")
            else:
                print(" ", end="")
        print()
main()