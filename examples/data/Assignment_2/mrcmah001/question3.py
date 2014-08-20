#Question 3
#Keanon Fell
#Program that calculates the area of a circle
import math
a=2
b= math.sqrt(2)
while (2/b) != 1 :
    a *= 2/b
    b= math.sqrt(2+b)
pi =a

print("Approximation of pi:",round(pi,3))
r = eval(input("Enter the radius:\n"))
a = round(pi*(r*r),3)
print("Area:",a)