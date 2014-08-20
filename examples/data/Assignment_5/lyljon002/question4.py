#Assignment 5, Question 4, creating a graph of a function
#LYLON002
#15 April 2014

import math
function = input("Enter a function f(x):\n")        #getting the function
display = ""                                        #preparing display string

for y in range(10,-11,-1):          #loop y values
    for x in range(-10,11):             #loop x values
        num=round(eval(function),0)
        if num == y:
            display = display + "o"
        elif y==0 and x==0:
            display = display + "+"
        elif x == 0:                        #outputting symbols into string
            display = display + "|"
        elif y == 0:
            display = display + "-"
        else:
            display = display + " "        
    display = display + "\n"    
print(display)                      #display output