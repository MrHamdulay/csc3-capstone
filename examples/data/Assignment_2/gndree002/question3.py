import math
def CalcPi():
    denom = math.sqrt(2)
    pie = 2
    count = 0
    while (2/denom != 1):
        pie = pie * (2/denom)
        denom = math.sqrt(2 + denom)
        count += 1
    print('Approximation of pi:', round(pie,3) )
    
    radius = eval(input('Enter the radius:\n'))
    area = pie * radius**2
    print('Area:', round(area,3))
        
CalcPi()    