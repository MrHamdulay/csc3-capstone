import math

denominator = math.sqrt(2)
a=2
y=2
while denominator<2:
    x = a/denominator
    y= x*y
    denominator = math.sqrt(2 + denominator)
    b = round(y,3)
    
print("Approximation of pi:",b)    
r = eval(input("Enter the radius:\n"))
area = float(y*(r**2))
c = round(area, 3)
print("Area:",c)



