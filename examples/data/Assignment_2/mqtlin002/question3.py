import math
t = math.sqrt(2) 
pi = 2 * (2/t) 
while (t!=2):
    t=math.sqrt(2+t)
    pi = pi * (2/t)

print ("Approximation of pi:",round(pi,3)) 
radius = eval(input("Enter the radius:\n")) 
print ("Area:",round((pi*(radius**2)),3))
