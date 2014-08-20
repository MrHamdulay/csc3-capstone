import math

denominator=math.sqrt(2)

a,b=2,2

while denominator<2:
    a1 = a/denominator
    b = a1*b
    c = round(b,3)    
    denominator = math.sqrt(2+denominator)
    
print("Approximation of pi:", c)
rad=eval(input("Enter the radius:\n"))
area=float(b*(rad**2))
ans = (round(area, 3))
print("Area:", ans)
    