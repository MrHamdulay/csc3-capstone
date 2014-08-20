"""
graphing program
Aaron Weinstein
16 April 2014
"""
import math
function = input("Enter a function f(x):\n")
for y in range (10,-11,-1):
    for x in range (-10,11):
        if y-0.5 <= eval(function) <= y +0.5:
            print("o", end ='')
        elif x==0 and y==0:
            print("+", end ='')
        elif x==0 and y!=0:
            print("|", end ='')
        elif x!=0 and y==0:
            print("-", end ='')
        else:
            print(" ", end='')
    print("")