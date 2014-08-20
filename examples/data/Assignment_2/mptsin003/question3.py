#Sinoxolo Mpetsheni
#MPTSIN003
#Assignment2
#CSC1015F

#Question3

import math


preDen = 0
pi = 2
nextTerm = 0

while nextTerm != 1:
    preDen = math.sqrt(2+preDen)
    pi*=2/preDen
    nextTerm = 2/preDen
    
       
print("Approximation of pi:",round(pi,3))
r = eval(input("Enter the radius:\n"))    
area =(pi)*(r)*(r)
print("Area:",round(area,3))