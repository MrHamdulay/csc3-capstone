import math

x=float(math.sqrt(2))
pi=2*(2/math.sqrt(2))

while x<2:
       
       y=x+2
       x=math.sqrt(y)
       pi=pi*(2/x)
       

print("Approximation of pi:", round(pi,3))
radius=float(input("Enter the radius:\n"))
answer=pi*(radius**2)
print("Area:", round(answer,3))