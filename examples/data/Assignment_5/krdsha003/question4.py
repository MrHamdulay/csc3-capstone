"""Assignment 5 question 4
Plot a graph using ascii art
Shaheen Karodia
KRDSHA003
2014-04-15"""
import math  


function=input("Enter a function f(x):\n")   #gets input from user

        
for y in range (10,-11,-1):   #maps out the y values of the grapth
        
        for x in range(-10,11,1):  #maps out the x values of the graph
                                           
                point=round(eval(function))    #rounds of each f(x) value of the function
                
                if point ==y :                #maps out graph with "o" symbols
                        print("o", end="")
                
                else:
                        
                        if x==0 and y==0:       #maps out the pount of the origin#
                                print("+", end=(""))
                                
                        elif x==0:
                                print("|", end="") #maps out the y axis
                        elif y==0:
                                print("-", end="") #maps out the x axis
                        else:
                                print(" ", end="") #maps out the hite space of the graph
        print()         #ensures the start of a nw line after every iteration of the inner loop
             
               
                     
        