
import math
def main():
    fx = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for r in range(10,-11,-1):
        for c in range(-10,11,1):
            x=c
            fy = round(eval(fx))
            if fy == r:
                print("o", end="")
            if r==0 and c==0 and  r != fy:
                print("+", end="")
            if c == 0 and r != 0 and r != fy:
                print("|", end="")
            if r==0 and  c!=0 and  r != fy:
                print("-", end="")
            else:
                if r != 0:
                    if c != 0:
                        if r != fy:
                            print(" ", end="")
        print()
main()