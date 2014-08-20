# Program to calculate area of a circle
# By Nasreen
# 11/03/14

import math

def pi_approx():
    x = 0
    y = 2
    while (x < 2):
        x = math.sqrt(2 + x)
        ans = 2/x
        y = ans*y
    pi = round(y, 3)
    print("Approximation of pi:", pi)
    
    rad = eval(input("Enter the radius:\n"))
    a = y*rad*rad
    print("Area:", round(a, 3))

pi_approx()
