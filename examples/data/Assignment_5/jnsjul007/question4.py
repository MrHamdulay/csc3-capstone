import math

function = input("Enter a function f(x):\n")

for i in range (10,-11,-1):
    for x in range (-10,11):
       
        graph = round(eval(function))
       
        if i == graph:
                    print("o",end="")       
        elif x == 0 and i == 0:
            print("+", end="")
        elif i == 0:
            print("-", end="")
        elif x == 0:
            print("|", end="")
        else:
            print(" ", end="")
    print()
            
        
        