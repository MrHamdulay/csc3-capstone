# Approximating PI and calculating circle area
# Kristin Kinmont
# 4 March 2014

import math
x=2
PI=2
term=0
while round(term,50)!=1:
    PI=PI*2/(math.sqrt(x))
    x=2+math.sqrt(x)
    term= 2/(math.sqrt(x))
print("Approximation of pi:",round(PI,3))
radius=eval(input("Enter the radius:\n"))
area= PI*(radius*radius)
area=round(area,3)
print("Area:",area)
      
    