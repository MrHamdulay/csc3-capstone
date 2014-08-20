#Phumelele Ndimande
#Assingment 2
#Question 3

import math

pi = 2
constant = math.sqrt(2)
x=2/constant

while x!= 1:
    pi=pi*x
    constant = math.sqrt(2+constant)
    x=2/constant

print("Approximation of pi:", round(pi,3))
radius= eval(input("Enter the radius:\n"))
Area = round((radius **2)*pi,3)
print("Area:", Area)