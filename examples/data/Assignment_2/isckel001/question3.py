#Using pi to calculate the area of a circle
#Done by: Kelly Isaacs
# 10-03-2014
 
#Used to activate sqrt function 
import math

# Defining variables
x=2 
y=math.sqrt(2)

# Creating a loop that stops when the next term is 1
while 2/y !=1:
    
    x= (x*(2/y)) # Multiplying 2 by pi
    
    y= math.sqrt(2+y) # Redefining the denominator

# The values that will be printed    
print("Approximation of pi:", round(x, 3))
value= float(input("Enter the radius:\n"))
print("Area:", round(x * value**2, 3))
