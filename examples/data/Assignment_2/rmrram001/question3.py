#Ramabulana Immanuel Ramaru
#student No.RMRRAM001
#CSC Assignment

from math import*
b= sqrt(2)
a=2
pi=2*(a/b)

while b<2:
    b=(sqrt(2+b))
    pi=(pi*a/b)    
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
print("Area:", round(r**2*pi,3))
