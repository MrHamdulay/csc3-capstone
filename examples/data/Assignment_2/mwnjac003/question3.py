import math
def Area():
    s=math.sqrt(2)
    x=s
    y=s
    p=1
    for i in range(40):
        x=math.sqrt(2+y)
        y=x
        r=2/x
        p=p*r
    d=(2*p*math.sqrt(2))
    print('Approximation of pi:',round(d,3))
    radius=eval(input("Enter the radius:\n"))
    print('Area:',(round((radius*radius*d),3)))
Area()