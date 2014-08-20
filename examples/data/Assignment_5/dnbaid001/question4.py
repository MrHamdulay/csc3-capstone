#Assignment 5 - Question 4
#Aidan de Nobrega
#13/04/2014

import math #For automatic marker to test

f = input("Enter a function f(x):\n") #User inputs a mathematical function in terms of x

for y in range(-10, 11): #10 to -10 on y-axis
    for x in range(-10, 11): #-10 to 10 on x-axis
        y_real = -y #flips y-axis
        if y_real == round(eval(f)): 
#if inverted y equals rounded value of function
            print("o", end="")
        else:
            if y_real == 0:
                if x == 0:
                    print ("+", end="") #origin
                else:
                    print ("-", end="") #x-axis
            elif x == 0:
                print("|", end="") #y-axis
            else:
                print(" ", end="") #whitespace
    print()              