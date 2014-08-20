"""Print a given graph function
Dudley Mutero
17-4-14"""

import math
a=input("Enter a function f(x):\n")

for y in range (10,-11,-1):
    for x in range (-10,11):
        if y-0.5<eval(a)<y+0.5:
            print ("o",end="") #print graph
        elif y ==0 and x==0:
            print ("+",end="")#print centre of graph
        elif x==0:
            print ("|",end="")#print y axis
        elif y==0:
            print ("-",end="")#print x axis
        
        else:
            print (" ",end="")   
    print ()      