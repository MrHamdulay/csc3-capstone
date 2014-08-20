#Author: NLXALE001
#Date: 17 April 2014
#Assignment 5

import math
#get input of funtion
function = input("Enter a function f(x):\n")

#create loop to go through each y value
for i in range (10, -11, -1):
    #create loop to go though each x value for given y value
    for x in range (-10, 11):
        y = eval(function)
        y = round(y)
        #check if graph hits this point
        if y==i:
            print ("o", end="")
        #check if this is the centre point
        elif i==0 and x==0:
            print ("+", end="")
        #check if position is x or y axis
        elif x==0:
            print ("|", end="")
        elif i==0:
            print ("-", end="")
        #else leave a blank space
        else:
            print (" ", end="")
    print ()
        
    
