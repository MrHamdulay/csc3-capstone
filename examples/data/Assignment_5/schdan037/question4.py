"""Daniel Schwartz
question 4
april 2014"""

# used for math functions inout by user
import math


def main():
    """main,
    receives input and prints out graph of function"""
    f = input("Enter a function f(x):\n")

    #nest for loop generates x, y values in ranges of graph
    for y in range(-10, 11):
        for x in range(-10, 11):
            y_real = - eval(f)

            if y == round(y_real):
                # puts o at graph point
                print("o", end="")
            elif (x == 0) and (y == 0):
                # puts a + in the centre
                print("+", end="")
            elif x == 0:
                # puts a | at the y axis
                print("|", end="")
            elif y == 0:
                # puts a - at the x axis
                print("-", end="")
            else:
                # fills empty spaces
                print(" ", end="")
        print() # new line

# runs main on entry
if __name__ == '__main__':
    main()