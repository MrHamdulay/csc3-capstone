import math

function = input("Enter a function f(x):\n")
x = 0
y = 0

for row in range(10,-11,-1):
    for column in range(-10,11,1):
        x=column
        
        fc = round(eval(function))
        
        if fc == row:
            print("o", end="")
            
        if row == 0 and column == 0 and row != fc:
            print("+", end="")
            
        if column == 0 and row != 0 and row != fc:
            print("|", end="")
            
        if row==0 and column != 0 and row != fc:
            print("-", end="")
            
        else:
            if row != 0:
                if column != 0:
                    if row != fc:
                        print(" ", end="")
                        
    print()