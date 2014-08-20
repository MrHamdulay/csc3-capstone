#Amitha Doodnath
#Student Number: DDNAMI001
#30 Second rule
#08/03/2014

import math

numerator=2
denominator=0
pi=2

count=1

while(denominator<2):

    denominator=math.sqrt(2 + denominator)
    term=numerator/denominator
    pi*=term
    count+=1
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=pi*(radius**2)
print("Area:",round(area,3))
    