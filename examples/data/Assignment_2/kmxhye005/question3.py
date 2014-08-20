import math

def areaofcircle():
    pi=2
    next=(math.sqrt(2))
    while (2/next) !=1:
        pi=pi*(2/next)
        next=math.sqrt(2+next)
        if 2/next==1: break
    print("Approximation of pi:",round(pi,3))
    r=eval(input("Enter the radius:\n"))
    print("Area:",round(pi*r**2,3))
    
    
areaofcircle()

    