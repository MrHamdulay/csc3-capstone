"""program to draw a function
Rivoningo Seweya
16 April 2014"""

import math
#function to determine y values
def y_values(x,formula):
    y_output=round(eval(formula.replace("x","("+str(x)+")")))
    y_output*=-1
    return y_output
#fuction that draws the graph
def DrawGraph():
    formula=input("Enter a function f(x):\n")
    y_inc=1//10
    formula=(formula)
    #loops to draw the graph
    for y in range(-10,11):
        for x in range(-10,11):
            if x==0 and y==0:
                if y-y_inc<=y_values(x,formula)<=y+y_inc==0:
                    print("o",end="")
                else:
                    print("+",end="")
            elif x==0:
                if y-y_inc<=y_values(x,formula)<=y+y_inc==y and x==0:
                    print("o",end="") 
                else:
                    print("|",end="")
            elif y==0:
                if y-y_inc<=y_values(x,formula)<=y+y_inc==0:
                    print("o",end="")
                else:
                    print("-",end="")
            elif y-y_inc<=y_values(x,formula)<=y+y_inc:
                print("o",end="")
            else:
                print(" ",end="")
        print()
            
DrawGraph()