#Adam Oosthuizen
#mymath
#17 April 2014
import math

def printGraph(a):
    ''' prints any f(x) function on a 10x10 grid'''
    for y in range(10,-11,-1):
        s= ''
        for x in  range(-10,11,1):
            y1 = round(eval(a))
            if round(y1)==y:
                s+= 'o'
            elif y == 0 and x ==0:
                s+='+'
            elif y == 0:
                s+='-'            
            elif x == 0:
                s+='|'         
            else:
                s+=' '
            
        print(s)
#prompt user for input
function = input("Enter a function f(x):\n")
#Call function
printGraph(function)