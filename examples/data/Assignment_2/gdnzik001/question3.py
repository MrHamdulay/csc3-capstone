#Godana Zikho   
#12 march 2014
#Program to approximate the value of pi and calculate the area of a circle

import math #executes the math library

#p=2*(2/math.sqrt(2))*(2/(math.sqrt(2+math.sqrt(2))))
#v1=math.sqrt(2)  #make a variable to store sqrt(2)
#v2=2/v1
count=0
pi = 2
v1 = math.sqrt(pi)
pi = pi*(pi/v1)
nextTerm = 100
#as long as the denominator is less than 2, keep adding sqrt(2)
while nextTerm>1:
    v1=math.sqrt(2+v1)
    nextTerm = 2/v1
    pi=pi*nextTerm
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
Area=pi*(radius**2)
print("Area:",round(Area,3))
