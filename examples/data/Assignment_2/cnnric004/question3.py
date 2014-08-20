import math

pi = 2*(2/math.sqrt(2))
denom = 0
count = 0

while (count!=1000):
  denom = math.sqrt(2+denom)
  pi = pi * (2/math.sqrt(2+denom))
  count+=1
  
rpi= round(pi,3)
print("Approximation of pi:",rpi)

radius = eval(input("Enter the radius:\n"))

print("Area:",round(pi*(radius*radius),3))