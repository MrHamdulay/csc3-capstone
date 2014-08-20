#pi
import math
def approfpi():
    x=math.pi
    y=round(x,3)
    print('Approximation of pi:',y)
    r=eval(input('Enter the radius:\n'))
    a=x*(r*r)
    z=round(a,3)
    print('Area:',z)


approfpi()