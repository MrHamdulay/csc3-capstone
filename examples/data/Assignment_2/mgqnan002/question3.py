# program to approximate the value of pi
# Auther: Nangamso Mgoqi
# Date: 14 March 2014 
 
import math
x = 2
y = math.sqrt(2)
z = 0
while z!=1:
    
    z= 2/y
   
    x = x*z
    y = math.sqrt(2+y)
    
print("Approximation of pi:", round(x,3))
r = eval(input("Enter the radius:\n"))
Area = x*r**2
print("Area:", round(Area,3))
