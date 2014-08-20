# Graph Plotter
# Irfan Habib
# 2014/04/17


def plot():
    import math
    f = input("Enter a function f(x):\n")
    
    for y in range(-10,11):
        for x in range(-10,11):
            y_real = -y
            fx = round(eval(f))
            if fx == y_real:
                print("o", end="")
            elif y_real==0 and x==0:
                print("+", end="")
            elif  x ==0:
                print("|", end="")
            elif y_real == 0:
                print("-", end="")
            else: print (" ",end="")
            
        print()
plot()
        