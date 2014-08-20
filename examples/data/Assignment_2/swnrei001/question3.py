from math import *

def getPi():
    pi = 2
    num = 2
    denom = sqrt(2)
    nextT = num/denom
    while nextT != 1:
        denom = sqrt(2 + denom)
        pi = pi * nextT
        nextT = num/denom
    return pi
        
PI = getPi()
print("Approximation of pi:", round(PI, 3))
print("Enter the radius:")
ans = eval(input())
print("Area:", round(PI * (ans**2), 3))