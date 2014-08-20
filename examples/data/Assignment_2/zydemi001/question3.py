#A program to work out the area of a circle, using pi and the radius of the circle
#Author: Emiel Zyde
#Date: 9 March 2014

import math
pi= 2
n= 2
i= 2
d= math.sqrt(2)
while i > 1:
        n= math.sqrt(n)
        i= 2/n
        n= 2+d
        d= math.sqrt(2+d)
        pi=pi*i
        
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
print("Area:", round(pi*(r**2),3))


