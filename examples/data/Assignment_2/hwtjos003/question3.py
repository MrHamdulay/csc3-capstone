import math
pi = 2.0
base = math.sqrt(2)
while(2/base != 1): 
    pi = pi * 2/base
    base = math.sqrt(2+base)
print("Approximation of pi:", round(pi,3))
rad = eval(input("Enter the radius:\n"))
print("Area:" , round(pi*rad*rad, 3))