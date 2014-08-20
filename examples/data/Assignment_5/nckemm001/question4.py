# Assignment 5: Question 4
# nckemm001
# 16 April 2014

import math
def main():
    function = input("Enter a function f(x):\n") # get input from user to enter function
    x = 0
    y = 0

    for graph in range(10,-11,-1):
        for g in range(-10,11,1):
            
            x=g
            fy = round(eval(function))
            
            if fy == graph:
                print("o", end="")
                
            if graph==0 and g==0 and  graph != fy:
                print("+", end="")
                
            if g == 0 and graph != 0 and graph != fy:
                print("|", end="")
                
            if graph==0 and  g!=0 and  graph != fy:
                print("-", end="")
                
            else:
                if graph != 0:
                    if g != 0:
                        if graph != fy:
                            print(" ", end="")
        print() #print the function
main()