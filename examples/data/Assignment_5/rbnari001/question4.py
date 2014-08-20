#Ariel Rubin
#RBNARI001
#16 April 2014
# a program to draw a graph of any given function

#imports math module
import math
#asks the user to enter a value for a function of x
function = input("Enter a function f(x):\n")
#following for loop goes around to create the grid
for y in range (10,-11,-1):
#2nd for loop prints out values relating to the graph    
    for x in range (-10,11):
        if y-0.5 <= eval(function) <= y +0.5:
            print("o", end ='')
        #prints + sign when both x and y values equal 0        
        elif x==0 and y==0:
            print("+", end ='')
        #prints | sign when x vale = 0 (y int)    
        elif x==0 and y!=0:
            print("|", end ='')
        #prints - sign when y vale = 0 (x int)   
        elif x!=0 and y==0:
            print("-", end ='') 
        else:
            print(" ", end='')
    print("")