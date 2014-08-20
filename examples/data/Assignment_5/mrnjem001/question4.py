import math
func=input("Enter a function f(x):\n")
for y in range(-10,11):
    for x in range(-10,11):
        if int(round(eval(func)))==-y:
            print("o", end="")
        elif y==0 and x==0:
            print("+",end="")
        elif y==0:
            print("-",end="")
        elif x==0:
            print("|", end="")
        else:
            print(" ", end="")
    print()
    