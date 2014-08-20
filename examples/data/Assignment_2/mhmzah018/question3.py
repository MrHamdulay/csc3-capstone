# Question 3
# Zaheer Mahmood
# Program to aproximae pi and area of circle

# To allow for pi to be approximated
import math
z=math.sqrt(2)
approx_PI=2
while(z!=2):
    approx_PI*=2/z
    
    z=z+2
    z=math.sqrt(z)
    

print("Approximation of pi:", round(approx_PI,3))
r=eval(input("Enter the radius:\n"))
print("Area:", round(approx_PI*r**2,3))