#Program to calculate value of PI then area of circle
#Palesa Magudulela
#14/03/2014

import math
x=math.sqrt(2)
y=2*2/x
while x!=2:
    x=math.sqrt(2+x)
    y=y*2/x
print("Approximation of pi:" ,round(y,3))
radius=eval(input("Enter the radius:\n"))
print("Area:" ,round(((radius**2)*y),3))