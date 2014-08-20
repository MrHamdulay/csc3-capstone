# question4.py
# a program to draw a text-based graph of a mathematical function f(x)
# Thomas Konigkramer
# 14 April 2014

import math

def grapher():
    function = input("Enter a function f(x):\n")
    
    
    for y in range(10,-11,-1):
        for x in range(-10,11):
           
            if round(eval(function)) == y:
                print("o", end = "")
            elif y == 0 and x == 0:
                print("+", end = "")            
            elif y == 0:
                print("-", end = "")
            elif x == 0:
                print("|", end = "")
            else:
                print(" ", end = "")
            
        print()
                
if __name__ == "__main__":
    grapher()