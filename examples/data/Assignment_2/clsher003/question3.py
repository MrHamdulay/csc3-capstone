#program to calculate the value of pi 
# 10 March 2014
import math

pi=2
base=math.sqrt(2)
new_term=2/base

while new_term!=1:
    pi=pi*new_term
    base=math.sqrt(2+base)
    new_term=2/base
print("Approximation of pi:",round(pi,3))

x=eval(input("Enter the radius:\n"))
y=pi*x*x
print("Area:", round(y,3))