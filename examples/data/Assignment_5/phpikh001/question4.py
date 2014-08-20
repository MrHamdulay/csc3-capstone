#Ikhlaas Pohplonker
#16 April 2014
#draws a text-based graph of a mathematical function f(x)
import math
mathematical_function=input("Enter a function f(x):\n")
for y in range(10,-11,-1):
    if y!=10:
        print("")
    for x in range(-10,11):
        function_value=eval(mathematical_function)
        function_value=round(function_value) #rounds the value of the mathematical function
        if y==function_value:
            print("o",end="")
        elif x==0 and y==0:
            print("+",end="")
        elif x==0:
            print("|",end="")
        elif y==0:
            print("-",end="")
        else: print(" ",end="")
        