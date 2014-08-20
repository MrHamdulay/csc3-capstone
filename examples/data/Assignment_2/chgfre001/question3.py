#program to get the value of pi
#by frederick chigwaza

import math
x=2
y=math.sqrt(2)
z=2
while z!=1:
    z=2/y
    y=math.sqrt(2+y)
    x=x*z
print("Approximation of pi:",(round((x),3)))
b=eval(input("Enter the radius:\n"))

a=x*b*b 
print("Area:",(round((a),3)))
