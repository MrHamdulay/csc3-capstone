# Question 4 prints out graph
# Jaren Hendricks
# 17 April 2014
import math 

# Users input
function = input("Enter a function f(x):\n")

# Loop for the x and y axis in the specified range. 
for y in range(10, -11, -1):
    for x in range(-10, 11):
        if y== (round(eval(function))):
            print("o", end= "") 
        elif y==0 and x==0:
            print("+", end="")
        elif y == 0:
            print("-", end ="")
        elif x == 0:
            print("|", end = "")
        else:
            print(" ", end = "")
    print()

        