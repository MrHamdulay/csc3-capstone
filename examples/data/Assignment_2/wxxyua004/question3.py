#question3

import math

import math

def circlearea():
    pi=2
    following=(math.sqrt(2))
    while (2/following) !=1:   
        pi=pi*(2/following)
        following=math.sqrt(2+following)
        if 2/following==1:
            break
    print("Approximation of pi:",round(pi,3))  
    r=eval(input("Enter the radius:\n"))
    print("Area:",round(pi*r**2,3))
circlearea()        