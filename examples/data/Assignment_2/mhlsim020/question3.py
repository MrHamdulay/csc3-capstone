# A program to calculate the Area of a circle using an approximation of Pi and a
# Radius entered by the user.
# Simlindile Mahlaba
# 14 March 2014
import math
t=math.sqrt(2)
Pi=(round((2)*((t)/2)*((t)+(t)/2)*((t+t+t)/2)*((t+t+t+t)/2)*((t+t+t+t+t)/2)*((t+t+t+t+t+t)/2),3))
print("Approximation of pi:", Pi)
Radius=print(input("Enter the radius: \n"))
Area=(Pi*Radius)
print(round(Area,3))
Print("Area:", Area)
