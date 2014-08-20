#Drawing a graph of a specific function
#Kayla Hendricks
#14 April 2014

import math
function=input("Enter a function f(x):\n")
x=0                     
y=0
for yaxis in range(10,-11,-1):          #perform for loop for xaxis on every y value
    for xaxis in range(-10,11):         
        x=xaxis                         #for every value of x on xaxis perform below functions
        point = round(eval(function))
        #statements for printing out graph
        if xaxis == 0 and yaxis == 0 and yaxis != point:
            print("+",end="")
        if xaxis == 0 and yaxis !=0 and yaxis != point:
            print("|",end="")
        if yaxis == 0 and yaxis != point and xaxis != 0:
            print("-",end="")
        if yaxis == point:
            print("o",end="")
        #if none of the above statments are true, create blank space
        else:
            if yaxis != 0:
                if xaxis != 0:
                    if yaxis != point:
                        print(" ",end="")
    print()
    
            
        
            
            