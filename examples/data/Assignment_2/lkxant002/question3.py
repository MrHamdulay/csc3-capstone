#Assignment 2
#Question 2
#LKXANT002

import math

plu=0
pi_=2
term=0

while term!=1:
    plu=math.sqrt(2+plu)
    term=2/plu
    pi_=pi_*term
    
print("Approximation of pi:",round(pi_,3))
rad=eval(input("Enter the radius:\n"))
area=pi_*rad*rad
print("Area:",round(area,3))