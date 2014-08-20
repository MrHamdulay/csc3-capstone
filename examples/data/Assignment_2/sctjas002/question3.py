import math
def areacalc():
    a=2
    b=math.sqrt(2)
    c=1
    while a/b>1:
        b=math.sqrt(2+b)
        c=c*a/b
    p=c*2*(2/math.sqrt(2))
    print("Approximation of pi:",round(p,3))
    r=eval(input("Enter the radius:\n"))
    area = p * r * r
    print("Area:", round(area,3))
areacalc()





                                        
