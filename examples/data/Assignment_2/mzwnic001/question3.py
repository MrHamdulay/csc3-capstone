import math
n=math.sqrt(2)
b=2
while n<2:
    a=2/n
    n=math.sqrt(2+n)
    b=b*a
    if n==2:
        c=round(b,3)
        print('Approximation of pi:',c)
        r=eval(input('Enter the radius:\n'))

        Area=(b)*(r**2)
        Area=round(Area,3)
        print('Area:',Area)
    
