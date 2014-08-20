"""Dzunisani Nyoni
16-April 2014
A program that find permutation"""

import math

b=input("Enter a function f(x):\n")

def function():
    #A function to draw a function between -10 and 10
    for y in range(10,-11,-1):
        for x in range (-10,11):
            g=eval(b.replace("x","("+str(x)+")"))
            if y==round(g):
                print("o",end="")             
            elif x== 0 and y== 0:
                print("+",end="")
            elif x==0 and y!= 0:
                print("|",end="")
            elif y== 0 and x!=0:
                print("-",end="")
            else:
                print(" ",end="")
        print()
        
def main ():
    function ()
if __name__ == "__main__":
    main ()
    
    
    
              