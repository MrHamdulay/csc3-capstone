#SNGSOH004
#Assignment 5
#Question4

import math

function=input("Enter a function f(x):\n")
array=[] #Defining the array variable

#Storing all points in the function that lie in the x interval [-10,10], however, we cannot store in negative intervals, so the points are stored from 0 to 21(exclusive of 21) and future for loops will take this into account by adding ten to any -10 index
for i in range(-10,11):
    x=i
    fx = round(eval(function))
    array.append(fx)
    
#The following for loop deals with plotting all points that lie above the x axis
for y in range (10,0,-1):
    for hz in range (-10,11):
        if(array[hz+10]==y):
            print("o",end="")
        elif(hz==0):
            print("|",end="")
        else:
            print(" ",end="")
    print()

#The following for loop deals with plotting all points that may or may not lie on the x axis
for newhz in range(-10,11):
    if (array[newhz+10]==0):
        print("o",end="")
    elif (newhz==0 and array[9]!=0):
        print("+",end="")
    else:
        print("-",end="")
print()
  
#The following for loop deals with plotting all points that lie below the x axis      
for y in range (-1,-11,-1):
    for hz in range (-10,11):
        if(array[hz+10]==y):
            print("o",end="")
        elif(hz==0):
            print("|",end="")
        elif(hz==0 and y==0):
            print("+",end="")
        else:
            print(" ",end="")
    print()
