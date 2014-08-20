#Program to draw a text-based graph of the mathematical function f(x).
#BRXCAI001
#16 April 2014

import math

#get an input for the function
function = input("Enter a function f(x):\n")

for y in range (10,-11,-1): #y-values in range of -10 to 10
    
    for x in range (-10,11): #x-values which fall inside the domain -10 to 10 
        num = eval(function)
        num_round = round(num)
        if x == 0 and y == 0 and num_round != 0: #origin
            print ("+", end='')
        elif x == 0 and num_round != y:
            print("|", end='') #y axis
        elif y == 0 and num_round != 0:
            print("-", end='') #x axis 
        elif y == num_round:
            print("o", end='') #plotting points
        else:
            print(" ", end='')
    print ()
    
            
            
            
            
            