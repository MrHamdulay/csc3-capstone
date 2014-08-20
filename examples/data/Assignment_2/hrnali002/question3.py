#A program that calculates PI and then the area of a circle
#Alison Hoernle
#HRNALI002
#9 March 2014

import math

#Calculate the value for PI here:
PI = 2
denominator = math.sqrt(2)
# In while loop
while(2/denominator != 1):
   # determine next term (Use the formula)
   PI = PI * (2/denominator)
   # update denominator to become new value
   denominator = math.sqrt(2 + denominator)
# We now have PI
print("Approximation of pi:", round(PI,3))
# get radius
radius = eval(input("Enter the radius:\n"))
area = PI * radius ** 2 
#print area
print("Area:", round(area, 3))