#TSOTETSI LERATO
#TSTLER003

from math import*
x=sqrt(2)
a=2
pi=2*(a/x)
while x<2:
    x=(sqrt(2+x))
    pi=(pi*a/x)
print("Approximation of pi:",round(pi,3))
c=eval(input("Enter the radius:\n"))
print("Area:",round(c**2*pi,3))