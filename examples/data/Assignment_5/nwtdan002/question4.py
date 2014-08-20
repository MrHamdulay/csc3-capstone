"""Drawing a graph of any inputted function
By Daniel Newton
13/04/14"""

import math     #Imported in case of any inputs using mathematical operations like sqrt.

func=input("Enter a function f(x):\n")  #Prompt user to enter a function in terms of x

for y in range(10,-11,-1):  #Evaluation of every y-value
    for x in range(-10,11): #And every x-value per y-value
        func2=round(eval(func),0)   #Evaluating the value of the function at the point in the loop to the nearest whole number.
        
        if func2==y:    #Check if function value is equal to y in the loop.   
            print("o",end='')

        elif x==0 and y==0: #make a '+' at (0,0)
            print("+",end='')

        elif y==0:          #make '-' along the x-axis
            print("-",end='')

        elif x==0:          #make '|' along the y-axis
            print("|",end='')

        else:               #Fill all others with a space
            print(" ",end='')

        if x==10:   #At the end of each row, move down to a new row.
            print()