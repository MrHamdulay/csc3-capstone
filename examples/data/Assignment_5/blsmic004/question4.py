''' program to display a mathematical function on an ascii graph
Michele Balestra BLSMIC004
17 April 2014'''

import math

#gets equation from user
funct = input("Enter a function f(x):\n")

#Evaluates function given by user
def fx(a):
    return (eval(funct)*-1)

#prints graph
yinc = 1/2
for y in range(-10,12):
    for x in range(-10,11):
        
        if y-yinc <= fx(x) <= y+yinc:
            print("o",end='')          
        elif x==0 and y==0:
            print ("+",end="")      
        elif x== 0:
            print ("|",end='')
        elif y== 0:
            print ("-",end="")
        elif x==10:
            print()
        elif y==1:
            print()
            break
        else:
            print(' ',end='')