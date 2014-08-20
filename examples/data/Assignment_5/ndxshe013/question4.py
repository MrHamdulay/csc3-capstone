
import math
f = input("Enter a function f(x):\n")

for i in reversed(range(-10,11)):
    for x in range(-10,11):
        if round(eval(f)) == i:
            print("o",end="")
        elif i == 0 and x == 0:
            print("+",end="")
        elif i == 0:
            print("-",end="")
        elif x == 0:
            print("|",end="")
        else:
            print(" ",end="")
    print()
