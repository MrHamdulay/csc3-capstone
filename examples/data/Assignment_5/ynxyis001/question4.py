#Question 4: Draws functions (graphs)
#Jennifer Yuan
#16 April 2014

import math #for use in math functions
function = input("Enter a function f(x):\n") 

for y in range (10,-11,-1): #going backwards
        for x in range (-10,11): #all values from -10 to 10
                x_value = eval(function.replace("x","("+str(x)+")"))
                if y==round(x_value): #Co-ordinates on plane
                        print("o",end="")
                elif x==0 and y==0: #origin
                        print ("+",end="")
                elif x == 0 and y!=0: #x-axis
                        print ("|",end="")
                elif y==0 and x!=0: #y-axis
                        print("-",end="")
                else: #where function does not exist
                        print(" ",end="")
        print()
    
    