import math
pi=2
term=2
z=math.sqrt(2)
while term != 1:
    term=2/z
    pi=pi*term
    z=math.sqrt(2+z)
    
print("Approximation of pi:",round(pi,3))
radius= eval(input("Enter the radius:\n"))
Area= pi*radius**2
print("Area:",round(Area,3))