#Program to approximate pi and calculate the area of a circle(Assignment 2: Question 3)"
#Name: Lauren Denny
#Student Number: DNNLAU005
#Date: 10 March 2014

import math

PI=2
t=math.sqrt(2)

while (2/t)>1:
    PI=PI*2/t
    t=math.sqrt(2+t)
    
print("Approximation of pi:",round(PI*1000)/1000)
r=eval(input("Enter the radius:\n"))
A=PI*r**2
print("Area:",round(A*1000)/1000)