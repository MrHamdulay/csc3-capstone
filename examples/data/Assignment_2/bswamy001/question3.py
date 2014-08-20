import math 

x=2
y=math.sqrt(2)
while y!=2:
    x=x*(2/y)
    y=math.sqrt(2+y)
    
print("Approximation of pi:",round(x,3))
rad=eval(input("Enter the radius: \n"))
area= x*rad**2
print("Area:",round(area,3))
