import math
x=2
next_term=math.sqrt(2)
while (2/next_term)!=1:
    x*=2/next_term
    next_term=math.sqrt(2+next_term)
pi=x
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:"'\n'))
Area =(pi*(r)**2)
print("Area:", round(Area, 3))



