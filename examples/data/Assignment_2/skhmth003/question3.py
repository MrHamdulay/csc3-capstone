import math
a=1
b=0
for i in range(100):
    b=math.sqrt(2+b)
    a=a*(2/b)
print("Approximation of pi:",round(2*a,3))
x=eval(input("Enter the radius:\n"))
print("Area:", round(2*a*(x**2),3))