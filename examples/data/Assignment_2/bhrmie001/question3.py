import math

i=math.sqrt(2)
pi=2
while 2/i!=1:
    pi=pi*2/i
    i=math.sqrt(2+i)
print("Approximation of pi:", round(pi, 3))

r=eval(input("Enter the radius:\n"))
print("Area:", round(pi*r**2, 3))