#Question 4 assignment 5 program to draw a graph
#Shane Horsley
#14 April 2014

import math
equation = input("Enter a function f(x):\n")#get equation

for y in range (10,-11,-1): #range of graph
    for x in range (-10,11):#domain of graph
        x_string="("+str(x)+")" #in order to substitute values of domain in to the equation
        equation_real = equation.replace("x",x_string)
        x_real = eval(equation_real) #converting string in to number
        if round(x_real)==y: print("o",end="")  #if equation is equal to y-value 
        elif y==0 and x==0: print("+",end="") #origin 
        elif y==0: print("-",end="")   #x axis if no intercept at this point
        elif x==0: print("|",end="")  #y axis if no intercept at this point
        else: print(" ",end="")  
    print()