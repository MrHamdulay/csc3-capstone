import math

bottom=math.sqrt(2)
term=2/bottom
pi=2
x=0

while term!=1:
    term=2/bottom
    pi*=term
    bottom=math.sqrt(2+bottom)

print("Approximation of pi:",round(pi,3))
      
r=eval(input("Enter the radius:\n"))
area=pi*(r**2)
print("Area:",round(area,3))
