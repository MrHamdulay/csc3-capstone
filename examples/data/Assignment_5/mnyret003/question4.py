# A program that draws a graph
# Retselisitsoe Monyake
# 16 April 2014
import math  
def function():
    a=input("Enter a function f(x):\n") 
    yinc = 0.5
    for y in range(-10, 11): 
        got_x = False
        y1=-y  # as the graph would be upside down as it is starting at -10
        for x in range(-10, 11):
            b=eval(a) 
            if y1-yinc <= b <= y1+yinc: 
                print ("o",end="")
                got_x = True
            elif x==0 and y==0:       
                print ("+",end="")
            elif x == 0:
                print ("|",end="")
            elif y == 0:
                print ("-",end="")
            else:
                print (" ",end="")   
                got_x = False                 
        print() #printing result as it will be stored in the function 
        
function()