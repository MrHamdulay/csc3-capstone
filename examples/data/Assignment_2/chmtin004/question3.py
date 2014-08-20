#Program to calculate area of a circle given the radius
#Tinotenda Chemvura (CHMTIN004)
#09 March 2014

#__________________________Program starts here____________________________________
import math
#calculation for the value of Pi

d=math.sqrt(2)
x=2/d
Pi=2
while x!=1:
    Pi=Pi*x
    d=math.sqrt(2+d)
    x=2/d

print("Approximation of pi:",round(Pi,3))

r=eval(input("Enter the radius:\n"))

A=round((Pi*r**2),3)

print("Area:",A)

#_______________________________Program stops here_________________________________