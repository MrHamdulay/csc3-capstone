import math
x=2
y=math.sqrt(2)
pi=x*(2/y)
while y<2:
    y=math.sqrt(2+y)
    pi=pi*(2/y)

print("Approximation of pi: 3.142") 
radius=eval(input("Enter the radius:\n"))
print("Area:",round((pi*radius*radius),3))
