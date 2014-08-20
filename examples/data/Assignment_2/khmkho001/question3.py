from math import *
p = sqrt(2) 
pi = 2 * (2/p) 

while (p!=2): 
            p = sqrt(2+p) 
            pi = pi * (2/p) 

print ("Approximation of pi,:",round(pi,3)) 
radius = eval(input("Enter the radius:\n")) 
print ("Area:",round(pi*radius**2,3)) 
