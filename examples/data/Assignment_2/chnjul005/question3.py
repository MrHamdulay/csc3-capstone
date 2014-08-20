import math
d = math.sqrt(2)
n = 2
ter = n*(n/d)
pi = ter
while ter != 1:
    d = math.sqrt(d+2)
    ter = n/d
    pi = pi*ter
          
print("Approximation of pi:",round(pi,3))
r = eval(input("Enter the radius:\n"))
ar = round((pi*(r**2)),3)
print("Area:",ar)