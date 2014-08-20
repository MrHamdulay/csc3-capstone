import math

equation = input("Enter a function f(x):\n")
y=10
while y>=-10:
    x=-10
    while x<=10:
        z=round(eval(equation))
        if y==z:
            print("o", end="")        
        elif y==0 and x==0:
            print("+", end="")       
        elif x==0:
            print("|", end="")
        elif y==0:
            print("-", end="")
        else: 
            print(" ", end="")    
        x+=1
    y=y-1
    print()
