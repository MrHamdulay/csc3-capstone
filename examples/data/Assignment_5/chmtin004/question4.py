"""Program to plot a graph given a function of f(x)
Tinotenda Chemvura CHMTIN004
13 April 2014"""

import math
fn = input("Enter a function f(x):\n")

for j in range(10,-11,-1):                     #loop for the y values
    for i in range(-10,11,):                   #loop for the x values
        y_value = ("("+str(i)+")")
        nfn = fn.replace("x",y_value)          #replace the all the x values in the f(x) with the x value "i"
        y1 = eval(nfn)
        y2 = round(y1)
                
        if y2 == j :                           # if f(i) is equal to the current j value in the j loop, print "o"
            print("o",end = "")                
        
        elif i == 0 and j == 0:                # if for f(i) and j are zero, (the origin), print "+"
            print("+",end = "")        
        elif j == 0:                           # print the x axis border if f(i) is not zero
            print("-",end = "")
        elif i == 0:                           # print the y - axis if f(i) is not zero
            print("|",end = "")
            
        else:
            print(" ",end = "")
        
    print()
        
#_____________________Program Ends Here_____________________