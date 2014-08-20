import math
function=input("Enter a function f(x):\n")
for x in range(-10,11):
    eval(function)
for y in range(-10,11):
    for x in range(-10,11):
        y_real=-round(eval(function))
        x_real=x
        if x_real==0 and y==0 and not y_real==y:
            print("+",end="")
        elif x_real==0 and y_real!=y:
            print("|",sep="",end="")
        elif y==0 and y_real!=y:
            print("-",end="")
        elif y_real==y:
            print("o",end="")
        else:
            print(" ",end="")
    print()