import math
x =2* (2/math.sqrt(2))
d = math.sqrt(2)

while d!=2:
    y=2+d
    z=math.sqrt(y)
    n=(2/z)
    x=x*n
    d=z
    
print("Approximation of pi:",round(x,3))
radius=eval(input("Enter the radius:\n"))
print("Area:", round(x*(radius**2),3))

            
