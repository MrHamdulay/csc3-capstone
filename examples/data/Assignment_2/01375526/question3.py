import math

num = 2
den = math.sqrt(2)
pi = 2

while (num/den > 1):
   pi *= num/den
   den = math.sqrt (2+den) 
      
print ("Approximation of pi:",round (pi, 3))
radius = float (input ("Enter the radius:\n"))
print ("Area:",round (pi*radius*radius, 3))

