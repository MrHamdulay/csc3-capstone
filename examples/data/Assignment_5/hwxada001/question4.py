import math

def main():
    f = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for r in range(10,-11,-1):
        for c in range(-10,11,1):
            x = c
            roundfx = round(eval(f))
            if roundfx == r:
                print("o", end="")
            
            if r == 0 and not c == 0 and not r == roundfx:
                print("-", end="")                
            if c == 0 and not r == 0 and not r == roundfx:
                print("|", end="")
            if r == 0 and c == 0 and not r == roundfx:
                print("+", end="")
            elif not r == 0:
                    if not c == 0:
                        if not r == roundfx:
                            print(" ", end="")
        print()
main()