""" Program to draw a graph given a function
By Tinashe Choga
15 april 2014"""
import math  # so that it can work with other functions like sinx
def function():
    a=input("Enter a function f(x):\n") 
    yinc = 0.5
    for y in range(-10, 11): 
        got_x = False
        y1=-y  # as the graph would be upside down as it is starting at -10
        for x in range(-10, 11):
            b=eval(a) #converting string entered by user to number
            if y1-yinc <= b <= y1+yinc: #the range it must consider to plot a point
                print ("o",end="")
                got_x = True
            elif x==0 and y==0:       #midpoint of graph paper
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