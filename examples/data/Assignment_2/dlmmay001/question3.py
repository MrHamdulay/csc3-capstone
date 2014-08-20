import math
def pi():
    x = math.sqrt(2)
    term1 = 2
    while 2/x != 1:
        term = 2/x
        term1 *= term        
        x = math.sqrt(2 + x)
    print('Approximation of pi:',round(term1,3))
    radius = eval(input("Enter the radius:\n"))
    area = term1*radius**2
    print('Area:',round(area,3))
pi()