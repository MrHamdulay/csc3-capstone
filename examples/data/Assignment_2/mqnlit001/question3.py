#question 3
# 13 March 2014
#Author: Litha Maqungo

import math
pi = 2
x = math.sqrt(2)
while 2/x >1:
    pi= pi*2/x
    x = math.sqrt(2+x)
pie = round(pi,3)
print("Approximation of pi:",pie)
print("Enter the radius:")
radius=eval(input())
Area = pi*radius**2
print("Area:",round(Area,3))
