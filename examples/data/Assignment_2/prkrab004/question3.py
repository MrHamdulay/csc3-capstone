#Assignment 3
#Question 3
#Rabia Parker
#PRKRAB004

import math

x=2
next_term = math.sqrt(2)
while (2/next_term)!=1:
   x = x*(2/next_term)
   next_term = math.sqrt(2+next_term)
pi=round(x,3)
print("Approximation of pi:",pi)
r = eval(input("Enter the radius: " '\n'))
Area=(x*(r**2)) 
print("Area:", round(Area,3))






