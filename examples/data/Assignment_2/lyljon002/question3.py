#8 March 2014
#Assignment 2, Question 2
#Jonathan Leyland, LYLJON002

import math
i = 0
z = math.sqrt(2)
total = 2
j = math.sqrt(2)

while i < 2:    
    total = total* (2 / z)
    j = math.sqrt(2 + z)
    i = j
    z = j
    
pi = round(total, 3)
print("Approximation of pi:", pi)   
radius = eval(input("Enter the radius:\n"))
area = total*radius*radius
print("Area:", round(area, 3) )  