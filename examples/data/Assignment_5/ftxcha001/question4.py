# Chantel Foot
# Assignment 5, question 4

import math 

function = input("Enter a function f(x):\n")

for y in range (10,-11,-1): #10 to -10 so have to go to -11
    
          for x in range(-10,11): # -10 to 10 so have to go up to 11
                    x_value = eval(function.replace("x","("+str(x)+")"))
        
                    if y==round(x_value): 
                              print("o",end="") 
        
                    elif x == 0 and y == 0: # to print origin
                              print("+",end="")
        
                    elif x == 0 and y != 0: # to print y axis
                              print("|",end="")
            
                    elif y == 0 and x != 0: # to print x axis
                              print("-",end="")
                    else: 
                              print(" ",end="") # this is where there is no function 
            
          print()

            
            
            
        
    