import math
denom = 2
pi = 2
while 2/(math.sqrt(denom)) !=1:
    pi = pi*(2/math.sqrt(denom))
    denom = 2+math.sqrt(denom)
print ("Approximation of pi:", round(pi,3))
r = eval(input("Enter the radius:\n"))
print ("Area:", round(r*r*pi,3))