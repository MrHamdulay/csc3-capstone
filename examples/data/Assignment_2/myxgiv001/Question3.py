import math
denominator=math.sqrt(2)
term =2/denominator
pi = 2*(2/math.sqrt(2))

while term !=1:
    denominator=math.sqrt(2+denominator)
    term = 2/denominator
    pi = pi*term
print("Aproximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
area=pi*(r**2)
print("Area:",round(area,3))
       