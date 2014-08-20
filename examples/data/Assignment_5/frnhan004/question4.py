"""question 4 - Assignment 5
FRNHAN004
16 April 2014"""

import math #trig graphs can be formed
def main():
    function=input("Enter a function f(x):\n") #user input to draw a specific graph
    x=0
    y=0
    
    for y in range (10,-11,-1): 
        for x in range (-10,11,1):
            round_fx=round(eval(function))
            if round_fx==y: #wherever the (rounded) value of f(x) is equal to the y, output "o"
                print("o", end="")
            if x==0 and y==0 and not round_fx==y: #middle of axes, use 'is not' to test whether two objects are the same thing
                print("+", end="") 
            if x==0 and not y==0 and not round_fx==y: #y axis
                print("|", end="")        
            if y==0 and not x==0 and not round_fx==y: #x axis
                print("-", end="")   
            else:
                if not y==0:
                    if not x==0:
                        if not y==round_fx:
                            print(" ", end="") #when rounded value of f(x) is not equal to y, output a space       
        print()
main()