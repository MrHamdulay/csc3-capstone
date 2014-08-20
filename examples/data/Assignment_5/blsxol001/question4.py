# A program that draws a graph in the xy- plane in the range [-10,10]
# xola bilose
# 17/04/14

import math
#creating the xy-plane 
def main():
    function=input("Enter a function f(x):\n")
    for y in range(10,-11,-1):
        for x in range(-10,11):
            function_value=round(eval(function))
            if function_value==y:
                print('o',end="")
            elif x==0 and y!=0 :
                print("|",end="") 
            elif x==0 and y==0:
                print("+",end="")
            elif y==0 and x!=0:
                print("-",end="")
            else:
                print(" ",end="")
        print() # when a loop restarts a new line is beng printed
main()