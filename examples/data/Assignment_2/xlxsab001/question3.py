import math
a=2
b=2/math.sqrt(2)
c=2/math.sqrt(2+math.sqrt(2))
d=2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))
e=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))
f=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))
g=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))
h=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))
i=a*b*c*d*e*f*g*h
j=round(i,3)
print("Approximation of pi:",j)
radius=eval(input("Enter the radius:\n"))
area=radius*radius*math.pi
print("Area:",round(area,3))
