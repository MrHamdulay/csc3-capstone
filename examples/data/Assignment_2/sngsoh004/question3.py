import math

pi = 2
denominator = math.sqrt(2)
pi = 2*2/denominator
while(2/denominator!=1):
    denominator = 2+denominator
    denominator = math.sqrt(denominator)
    pi = pi*(2/denominator)
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
area=pi*(radius**2)
print("Area:",round(area,3))
