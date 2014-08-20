#program simulating a vending machine to calculate change
#gary Finkelstein
#15 April 2014

import math
#allow user to enter a function
user_function = input("Enter a function f(x): \n")

#create x and y axis, by printing "|" and "-", a "+" for the origin and print graph using "o" where y value is in domain of function
for y in range(10,-11,-1):
    
    if y!=10:
        print("")
    
    for x in range(-10,11):
        
        function = round(eval(user_function))
        
        if y == function:
            print("o", end="")
        elif x ==0 and y ==0:
            print("+", end="")
        elif y ==0:
            print("-", end="")
            
        elif x ==0:
            print("|", end="")
            
        else:
            print(" ", end="")
            