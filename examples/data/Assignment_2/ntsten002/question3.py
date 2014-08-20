import math
a= math.sqrt(2)
x=2

while (2/a) != 1:
    x=x*(2/a)
    a=math.sqrt(2+a)    
    
print("Approximation of pi:", round(x, 3))
radius=eval(input("Enter the radius:\n"))
area=round(x*(radius**2), 3)
print("Area:",area)