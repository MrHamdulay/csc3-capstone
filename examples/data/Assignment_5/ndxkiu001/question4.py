#Kiuran Naidoo
#Assignment 5
#Question 4
import math #import math for possible sin functions etc. 
fx=input("Enter a function f(x):\n") #Get user input

for y in range (10,-11,-1):
    for x in range (-10,11,1):
        value = round(eval(fx)) #Evaluate function and get a value
        if x == 0 and y == 0 and y != value: #Print origin
            print("+",end="")
        elif y == value: #Print a value of the function
            print("o",end="")
        elif y == 0: #Print horizontal axes
            print("-",end="")
        elif x == 0: #Print vertical axes
            print("|",end="")
        else: #Default option
            print(" ",end="")
    print() #Move to next line
