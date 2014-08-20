#Assignment 2, Question 3
#Pi and radius calculator
#Kieran Reilly
#RLLKIE001
#10/03/14


import math

sequence = math.sqrt(2)                         #squenced used to hold square root 2
formula = 2                                     #formula used to hold 2, and late the pi formula
pi = 2*2/math.sqrt(2)                           #beginning value of pi
while(formula > 1.0):
    sequence = math.sqrt(2 + sequence)
    formula = 2/sequence
    pi = pi*formula                             #calculating pi
    
    

print("Approximation of pi: "+str(round(pi, 3)))

radius = eval(input("Enter the radius: \n"))
area = pi * (radius)*(radius)

area = round(area, 3)
print("Area: "+str(area))

