import math
k = math.sqrt(2) 
pi = 2 * (2/k) 
while (k!=2):
    k=math.sqrt(2+k)
    pi = pi * (2/k)

print ("Approximation of pi:",round(pi,3)) 
rad = eval(input("Enter the radius:\n")) 
print ("Area:",round((pi*(rad**2)),3))
