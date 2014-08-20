import math
def main():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for rows in range(10,-11,-1):
        for column in range(-10,11,1):
            x=column
            roundfunction = round(eval(function))
            if roundfunction == rows:
                print("o", end="")
            if rows==0 and column==0 and not rows == roundfunction:
                print("+", end="")
            if column == 0 and not rows == 0 and not rows == roundfunction:
                print("|", end="")
            if rows==0 and not column==0 and not rows == roundfunction:
                print("-", end="")
            else:
                if not rows == 0:
                    if not column == 0:
                        if not rows == roundfunction:
                            print(" ", end="")
        print()
main()