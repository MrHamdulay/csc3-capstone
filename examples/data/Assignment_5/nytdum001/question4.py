import math
def main():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0
#range from 10to(-11) for axis graphing,and covers range from -10to10
    for rows in range(10,-11,-1):
        for columns in range(-10,11,1):
            x=columns#ie y-axis values
            roundfx = round(eval(function))
            if roundfx == rows:#ie x-axis values
                print("o", end="")
            if rows==0 and columns==0 and not rows == roundfx:
                print("+", end="")#for where the axis intersect
            if columns == 0 and not rows == 0 and not rows == roundfx:
                print("|", end="")
            if rows==0 and not columns==0 and not rows == roundfx:
                print("-", end="")
            else:
                if not rows == 0:
                    if not columns == 0:
                        if not rows == roundfx:
                            print(" ", end="")
    
        print()
main()