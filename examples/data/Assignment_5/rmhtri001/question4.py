import math
def GraphPrinter():
    fx = input("Enter a function f(x):\n")
    x = ""
    y = ""
   
    for xaxis in range(10,-11,-1):
        for yaxis in range(-10,11,1):
            x = yaxis
            yvalue = round(eval(fx))
            if yvalue == xaxis:
                print("o", end="")
            elif xaxis==0 and yaxis==0 and xaxis != yvalue:
                print("+", end="")
            elif yaxis == 0 and xaxis != 0 and xaxis != yvalue:
                print("|", end="")
            elif xaxis==0 and yaxis!=0 and xaxis != yvalue:
                print("-", end="")
            else:
                if xaxis!=0 and yaxis!=0 and xaxis != yvalue:
                    print(" ", end="")
        print()
GraphPrinter()
        