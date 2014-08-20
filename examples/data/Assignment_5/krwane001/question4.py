import math
def main():
    graph=input("Enter a function f(x):\n")
    x=0
    y=0
    for row in range(10,-11,-1):
        for col in range(-10,11,1):
            x=col
            roundfa=round(eval(graph))
            if roundfa == row:
                print("o", end="")
            if row == 0 and col == 0 and not row == roundfa:
                print("+", end="")
            if col == 0 and not row == 0 and not row == roundfa:
                print("|", end="")
            if row == 0 and not col == 0 and not row == roundfa:
                print("-", end="")
            else:
                if not row == 0:
                    if not col == 0:
                        if not row == roundfa:
                            print(" ", end="")
        print()
main()