# This program calculates pi and area of a circle
# by: SLLMOG004

import math
i=0
while i<1:
    i = round((2/(1+i))*2/math.sqrt(2)*2/math.sqrt(2+math.sqrt(2))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))), 3)
    print("Approximation of pi:", i)
    r=eval(input("Enter the radius:\n"))
    print("Area:", round(math.pi*r**2, 3))