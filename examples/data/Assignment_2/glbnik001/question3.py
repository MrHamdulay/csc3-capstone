import math
def piproxcirc():
    z=2
    x=math.sqrt(2)
    y=1
    while z/x>1:
        x=math.sqrt(2+x)
        y=y*z/x
    a=y*2*(2/math.sqrt(2))
    print("Approximation of pi:", round(a,3))
    x = eval(input ("Enter the radius:\n"))
    area = a*x*x
    print ("Area:", round(area,3))
piproxcirc()