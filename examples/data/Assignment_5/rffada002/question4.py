import math
function = input("Enter a function f(x):\n")
x = 0
y = 0

for y_axis in range(10,-11,-1):
    for x_axis in range(-10,11,1):
        x=x_axis
        round_ = round(eval(function))
        if round_ == y_axis:
            print("o", end="")
        if y_axis==0 and x_axis==0 and y_axis != round_:
            print("+", end="")
        if x_axis == 0 and y_axis != 0 and y_axis != round_:
            print("|", end="")
        if y_axis==0 and x_axis!=0 and y_axis != round_:
            print("-", end="")
        
        else:
            if y_axis != 0:
                if x_axis != 0:
                    if y_axis != round_:
                        print(" ", end="")
    print()