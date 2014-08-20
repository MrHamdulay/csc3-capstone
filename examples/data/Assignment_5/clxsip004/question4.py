#Siphesihle Cele
#assignment 5
#program to draw a cartesien axis and a function graph inputed by user

import math

graph=input("Enter a function f(x):\n") #user inputs the function he wishes to draw on the cartesien plane.

for y in range(10,-11,-1):
    for x in range(-10,11):
        func=round(eval(graph))
        if func ==y:
            print('o',end="")
        elif x==0 and y!=0:
            print('|',end="")
        elif y==0 and x!=0:
            print('-',end="")
        elif x==0 and y==0:
            print('+',end="")
        else:
            print(' ',end="")
    print()
        

               
    


