# Program to graph functions
# Nevarr Pillay - PLLNEV006
# 12 April 2014

import math

def graph(function):    
    for y in range(10,-11,-1):
        for x in range(-10,11): 
            fx = round(eval(function))
            if fx == y:
                print("o",end="")
            elif x == 0 and y == 0:
                print("+",end="")                
            elif x == 0:
                print("|",end="")
            elif y == 0:
                print("-",end="")            
            else:
                print(" ",end="")
        print()
    
def main():
    func = input("Enter a function f(x):\n")
    graph(func)
        
main()        