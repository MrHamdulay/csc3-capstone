def graph():
    import math
    for y in range (10,-11,-1):
        for x in range (-10,11):
            if y==round((eval(fx))):
                print("o",end="")
            elif y==0 and x==0:
                print("+",end="")
            elif y==0:
                print("-",end="")   
            elif x==0:
                print("|" ,end="")
            else:
                print(" ",end="")
        print()
fx=input("Enter a function f(x):\n")
graph()