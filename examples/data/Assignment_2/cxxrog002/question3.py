import math
x=2
y=math.sqrt(2)
pi=x*(2/y)
while y<2:
    y=math.sqrt(2+y)
    pi=pi*(2/y)

print("Approximation of pi: 3.142")
r=eval(input("Enter the radius:\n"))
area=round(((r**2)*pi),3)
print("Area:",area)