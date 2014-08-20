#Sipho Ngqayimbana
#Program calculating area
#10 March 2014

import math
pi = 2
deno = 0
num = 0
while num != 1:
    deno = math.sqrt(deno+2)
    num = 2/deno
    pi *= num
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius: \n")) 
area = pi*(radius**2)
print("Area:",round(area,3))
              