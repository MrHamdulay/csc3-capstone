import math
h = math.sqrt(2) 
pi = 2 * (2/h) 
while (h!=2):
    h=math.sqrt(2+h)
    pi = pi * (2/h)

print ("Approximation of pi:",round(pi,3)) 
rad = eval(input("Enter the radius:\n")) 
print ("Area:",round((pi*(rad**2)),3))
