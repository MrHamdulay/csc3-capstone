import math
i=math.sqrt(2)
pi=2*2/i
while(i!=2):
    i=math.sqrt(2+i)
    pi*=2/i
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=pi*radius**2
print("Area:",round(area,3))