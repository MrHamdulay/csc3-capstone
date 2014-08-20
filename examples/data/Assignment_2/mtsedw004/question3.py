import math
v=math.sqrt(2)
value_of_pi=2*(2/v)
while v!=2:
    v=math.sqrt(2+v)
    value_of_pi=value_of_pi*(2/v)
print("Approximation of pi:",end=" ")
print(round(value_of_pi,3)) 
radius=eval(input("Enter the radius:\n"))
print("Area:",end=' ')
print(round(radius**2*value_of_pi,3))