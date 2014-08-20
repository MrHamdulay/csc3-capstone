
a=2
import math
b=2/math.sqrt(2)
c=2/math.sqrt(2+math.sqrt(2))
d=2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))
e=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))
f=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))
g=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))
h=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))
i=2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))
pi=a*b*c*d*e*f*g*h*i
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=pi*(radius**2)
print("Area:",round(area,3))     