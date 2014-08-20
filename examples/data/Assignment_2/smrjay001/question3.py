from math import *
j=2
x = 0
i = (2/sqrt(2 + x))
while i!=1:
    j *= i 
    x = sqrt(2+x)
    i = (2/sqrt(2+x))
print("Approximation of pi:", round(j,3))
r = eval(input("Enter the radius:\n"))
area = pi*r*r
print ("Area:",round(area,3))