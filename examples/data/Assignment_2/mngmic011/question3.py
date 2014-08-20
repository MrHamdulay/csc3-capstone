#area of circle

import math
i=math.sqrt(2)
denom=1
pi=2
while denom<2:
        denom=i
        k=(2/denom)
        pi=(pi*k)
        i=(math.sqrt(2+(i)))
piround=round(pi,3)
print("Approximation of pi:", piround)
radius=eval(input("Enter the radius:" "\n"))
area=round((pi*(radius*radius)),3)
print("Area:", area)
