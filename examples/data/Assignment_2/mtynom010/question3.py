#A computer that calculates the valuue of pi and are of a cicle
#by Nomvuzo Matya
from math import*
x=sqrt(2)
pi=2*(2/x)
while (x!=2):
    x=sqrt(2+x)
    pi=pi*(2/x)
print("Approximation of pi:",round(pi,3))
rad=eval(input("Enter the radius:\n"))
print("Area:",round(rad**2*pi,3))