#Author:Percival Munhuwaani
#Date:16/04/2014
#Program: A program to draw a text-based graph of a mathematical function f(x).

import math
def main():
    function=input("Enter a function f(x):\n") #Putting the name of the function
    #Drawing the graph
    for y in range(10,-11,-1):
        for x in range(-10,11,1):
            f=round(eval(function))
            if f==y:
                print("o",end="")
            elif ( x==0 and y!=f and y!=0):
                print("|",end="")
            elif ( x==0 and y==0 and y!=f ):
                print("+",end="")
            elif ( y==0 and y!=f and x!=0):
                print("-",end="")
            else:
                print(" ",end="")
        print()
main()
                
    
    
    