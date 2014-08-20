"""Drawing of functions
Kumaran Reddy
16 April 2014"""

import math  
    
def graph():
    Function=input("Enter a function f(x):\n")
    for y in range(-10,11):
        for x in range(-10,11):
            function = round(eval(Function))
            if -function==y:
                print("o",end='')                       
            elif x==0 and y==0:
                print ("+",end="")
            elif x==0:
                print ("|",end="")
            elif y==0:
                print ("-",end="")
            else:
                print (" ",end="")
        print ()              
    
graph()