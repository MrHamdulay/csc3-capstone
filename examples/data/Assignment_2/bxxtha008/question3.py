#Author: Thabiso Beau
#question3.py
from math import * 

v = sqrt(2) 
pi = 2 * (2/v)

while (v!=2):
    v= sqrt(2+v)
    pi = pi * (2/v) 
print ("Approximation of pi:",round(pi,3))
radvalue = eval(input("Enter the radius:\n")) 
print ("Area:",round((pi*(radvalue)**2),3)) 
