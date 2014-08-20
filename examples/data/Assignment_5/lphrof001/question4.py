""" program to graph a mathematical function"""
#Author: Rofhiwa Liphauphau
#Date: 15 April 2014

import math

        

def graph():
    yinc=1/10
    function=input("Enter the function f(x):\n") 
    for y in range(10,-11,-1):# for the columns
        for x in range(-10,11,1):#for the rows 
            y_actual=-1 #change the range such that it goes from 10 to -10 at the bottom because it was the incorrect way around
            x_actual=-1
            func_tion=round(eval(function))
            if x_actual==0 and y_actual==0:
                print("+",end="")
            elif x_actual==0:
                print("|",end="")
            elif y_actual==0:
                print("-",end="")
            elif y_actual-yinc<= func_tion<=y_actual+yinc:
                print("o",end="")
            else:
                print(" ",end="")
            
        

graph()
