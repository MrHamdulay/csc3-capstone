import math
t=0
g=2

while t != 2:
   g=g*(2/math.sqrt(2+t))
   t=(math.sqrt(2+t)) 
print("Approximation of pi:",round(g,3))  
y=eval(input("Enter the radius:"))
area = g*(y*y)
print("\nArea:",round(area,3))