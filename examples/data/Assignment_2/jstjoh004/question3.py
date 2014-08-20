#pi program

import math

nextterm = 1
x = math.sqrt(2)
pi = 2*x
term = 2
while term > 1:
    y = math.sqrt(2+x)
    nextterm = y
    x=y
    term = 2/nextterm
    pi = pi*term
    
print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))
print("Area:",round(rad*rad*pi,3))
    

    
    

