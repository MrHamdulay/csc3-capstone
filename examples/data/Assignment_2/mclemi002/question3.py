#emile mclennan
#9/3/14
#Q3

import math


a=0
b=1
pi=2


while a != 2:
    a=math.sqrt(2+a)
    b=2/a
    pi=pi*b
    
   
print("Approximation of pi:",round(pi,3))
rad=eval(input("Enter the radius:\n"))

area = round(pi*(rad**2),3)
print("Area:",area)
