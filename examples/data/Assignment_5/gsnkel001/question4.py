# Question 4
# Kelly Goosen
# 2014/04/16

import math

function = input("Enter a function f(x):\n") #backwards

for y in range(10,-11,-1): #values from -10 to 10
        for x in range(-10,11):
                x_value = eval(function.replace("x","("+str(x)+")"))
                if y==round(x_value): #co-ordinates
                        print("o", end="")      
                elif y==0 and x == 0: #origin
                        print("+", end="")
                elif x==0 and y !=0: #x-axis
                        print("|", end="")
                elif y==0 and x != 0: #y-axis
                        print("-",end="")    
                else: #where function doesn't exists
                        print(" ", end="")
        print()