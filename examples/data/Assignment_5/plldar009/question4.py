import math

import math
def main():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for rows in range(10,-11,-1):
        for column in range(-10,11,1):
            x=column
            rounded = round(eval(function))
            if rounded == rows:
                print("o", end="")
            if rows==0 and column==0 and not rows == rounded:
                print("+", end="")
            if column == 0 and not rows == 0 and not rows == rounded:
                print("|", end="")
            if rows==0 and not column==0 and not rows == rounded:
                print("-", end="")
            else:
                if not rows == 0:
                    if not column == 0:
                        if not rows == rounded:
                            print(" ", end="")
        print()
main() 