# a program to sketch a graph
# mashau zwivhuya
# 15 March 2013
import math
# getting input
function=input("Enter a function f(x):\n")
function=function.replace("^","**")
# drawing the graph
def graph():
    #drawing the axes
    for xx in range(10,-11,-1):
        for yy in range(-10,11,1):
            x=yy
            func=round(eval(function))
            if  xx==func:
                print("o",end='')
            if yy==0 and xx==0 and not func==xx:
                print("+",end='')
            # drawing y axis     
            if yy==0 and not xx==0 and not xx==func:
                print("|",end='')
            # drawing x axis    
            if xx==0 and not yy==0 and not xx==func:
                print("-",end='')
            else:
                if not xx==0 and not yy==0 and not xx==func:
                    print(" ", end='')
        print()
graph()