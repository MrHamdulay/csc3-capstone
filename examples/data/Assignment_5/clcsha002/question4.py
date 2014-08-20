"""question 4 of assignment 5
shannon clacey
15 april 2014"""
import math

blank = "" #empty variable to be used later
origin = "+"
x_axis = "-"
y_axis = "|"
plotted_points = "o" 

#get input of the function to be plotted by the program
equation = input("Enter a function f(x): \n")

for y in range (10, -11, -1): #looking at the possible y values where y is equal to the max value of y 
    if y != 10:
        print (blank)
    
    for x in range (-10, 11): #looking at the x values which fall inside the domain -10 to 10 and still lie in the range of y 
        value = eval(equation) #looking at the numerical value of equation put in
        value_round = round(value)
        if x == 0 and y == 0 and value_round != 0: #sketching origin
            print (origin, end=blank)
        elif x == 0 and value_round != y:
            print (y_axis, end=blank) #sketching y axis
        elif y == 0 and value_round!= 0:
            print (x_axis, end=blank) #sketching x axis
        elif y == value_round:
            print (plotted_points, end=blank) #plotting actual graph given by user
        else: print(" ", end='')
    
     