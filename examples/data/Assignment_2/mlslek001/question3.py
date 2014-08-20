import math
pi=2
b=math.sqrt(2)
c=pi/b

#print("Approximation of pi: ",pi)
while c!= 1:
    pi=pi*c
    b=math.sqrt(2+b)
    c=2/b
    
print("Approximation of pi:",round(pi,3))
t=eval(input("Enter the radius:\n"))
area=pi*t**2
print("Area:", round(area,3))