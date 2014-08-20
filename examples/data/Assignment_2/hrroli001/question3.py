import math
i=math.sqrt(2)
x=2
while (2/i)!=1:
    c=2/i
    y=x*c
    x=y
    i=math.sqrt(2+i)

pi=x
print("Approximation of pi:",round(pi, 3))
rad=input("Enter the radius: \n")
area1=(pi)*((eval(rad))**2)
area2=round(area1, 3)
print("Area:",area2)