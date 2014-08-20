#Assignment 2
#Question 3
#pi
import math
pi=2
n=2
i=2
d=math.sqrt(2)
while i>1:
    n=math.sqrt(n)
    i=2/n
    pi=pi*i
    n=2+d
    d=math.sqrt(2+d)
print("Approximation of pi:", round(pi,3),sep=" ")
r=eval(input("Enter the radius:\n"))
print("Area:", round(pi*(r**2),3), sep=" ")
