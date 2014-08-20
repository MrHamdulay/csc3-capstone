from math import*
PI=2
y=sqrt(2)
while 2/y!=1:
    PI=PI*2/y
    y=(sqrt(2+y))
print("Approximation of pi:",round(PI,3))
question=eval(input("Enter the radius:\n"))
area=PI*(question)**2
area1=round(area,3)
print("Area:",area1)