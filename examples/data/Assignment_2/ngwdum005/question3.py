#Dumisani Ngwenza
#NGWDUM005
#09/03/14
#A program that calculates the value of PI and computes and then displays the area of a circle with a radius entered by the user.

import math

#a = math.sqrt(2)

numerator = 2
denominator = math.sqrt(2)
ratio = numerator/denominator
pi = 2

while ratio != 1:
    pi = pi * ratio
    denominator = math.sqrt(2+denominator)
    ratio = numerator/denominator
    
print ("Approximation of pi:", round(pi,3))
radius = eval (input("Enter the radius: \n"))
area = round(pi * (radius)**2,3)
print ("Area:", area)