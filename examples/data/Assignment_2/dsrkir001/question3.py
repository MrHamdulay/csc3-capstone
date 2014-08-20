import math

denominator = math.sqrt(2)
a=2
y=2
while denominator<2:
    x = a/denominator
    y= x*y
    denominator = math.sqrt(2 + denominator)
b =(round(y,3))
print("Approximation of pi:",b)    
r = float(eval(input("Enter the radius:\n")))
ans = (y*(r*r))
print("Area:",(round(ans,3)))




