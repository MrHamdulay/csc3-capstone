
import math

def function_graph():
    v_form = input("Enter a function f(x):\n")
    for y in range (10,-11,-1):
        for x in range(-10,11):
            real_y = round(eval(v_form))
            if y == real_y:
                print("o",end="")
            elif x == 0 and y == 0:
                print("+",end="")
            elif x == 0:
                print("|", end="")
            elif y == 0:
                print("-",end="")
            else:
                print(" ",end="")
        print()
function_graph()