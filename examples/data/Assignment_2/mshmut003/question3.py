# Approximation of pi
# Assignment 2
# Mutali Mashamba
import math

def pi():
    x=math.sqrt(2)
    y=2/x
    pi=2*y
    while y != 1:
        x=math.sqrt(2+x)
        y=2/x
        pi=pi*y
    print('Approximation of pi:',round(pi,3))
    rad=eval(input('Enter the radius:\n'))
    if rad>=0:
        area=pi*(rad**2)
        area=round(area,3)
        print('Area:',area)
pi()