"""program to draw a function entered by user
nosipho khumalo
15 April 2014"""
import math
def graph():
    function = input("Enter a function f(x): \n")
    for y in range(10,-11, -1):
        for x in range(-10,11):
            #function = eval(function)
            if round(eval(function)) == y:
                print("o", end ="")
            elif x == 0 and y == 0:
                print("+", end="")            
            elif x == 0:
                print("|", end ="")
            elif y == 0:
                print("-", end = "")
            else: print(" ", end = "")
        print()
graph()           