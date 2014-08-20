import math
y = math.sqrt(2) 
pi = 2 * (2/y) 
while (y!=2):
    y=math.sqrt(2+y)
    pi = pi * (2/y)

print ("Approximation of pi:",round(pi,3)) 
rad = eval(input("Enter the radius:\n")) 
print ("Area:",round((pi*(rad**2)),3))
