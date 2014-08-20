#Litha Maqungo
#Question 4
import math
print("Enter a function f(x):")
function=input() #allows the user to enter the function of the graph

for y in range (10, -11, -1): #setting the range for the program in decreasing order (range)
    if y != 10:
        print ("")
        
    for x in range(-10,11): #increasing order (setting domain of the function)
        coordinates=round(eval(function))#this is f(x), with the explicit points only
        if x == 0 and y == 0 and coordinates != 0: #this is the origin
            print("+", end ='')
        elif y == 0 and coordinates != 0 : #thisis the x axis
            print("-", end ='') 
        elif x == 0 and coordinates != y: #for the y axis
            print("|",end='')
        elif y == coordinates: 
            print("o", end ='')
        else:
            print(" ", end ='')