#Kekolo Phetla
#PHTKEK001
#Assignment 2

import math

pi=2
t1=2
a=2
d=math.sqrt(2)

while a>1:
    t1=math.sqrt(t1)
    a=2/t1
    t1=2+d
    d=math.sqrt(2+d)
    pi=pi*a
    
print("Approximation of pi:", round(pi,3))
radius=eval(input("Enter the radius: \n"))
print("Area:", round(pi*(radius**2),3))


