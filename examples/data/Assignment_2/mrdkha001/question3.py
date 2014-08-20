# Question 3
# Name: Khanyisile Morudu
# Student Number: mrdkha001
# Date: 07/03/2014
import math
import time

b = math.sqrt(2)
a = 2/b
pi = 2
while a != 1:
    pi = pi * a
    b= math.sqrt(2 + b)
    a = 2/b

def Area_Check():
    print("\nApproximation of pi: "+ str(round(pi, 3)))
    n = eval(input("Enter the radius:\n"))
    Area = pi * (n**2)
    print("Area:", round(Area,3))
Area_Check()
