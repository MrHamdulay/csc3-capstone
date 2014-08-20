def pi():
    import math
    import time
    d=math.sqrt(2)
    term=(2/math.sqrt(2))
    pie=2*term
    while d!=2.0:
        d1=math.sqrt(2+d)
        term2=(2/d1)                
        pie1=pie*term2
        d=d1
        pie=pie1
    print("Approximation of pi:",round(pie,3))
    r=eval(input("Enter the radius:\n"))
    area=round(pie*r**2,3)
    print("Area:",area)
pi()
