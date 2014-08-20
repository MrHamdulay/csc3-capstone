# program to find the value of PI and calculate area

# Name: Matthew Bandama

# Student Number: BNDTAT003

# Date: 13-Mar-2014

import math

a = 2

b = math.sqrt(a)

c = 2*(2/b)

while b != 2:
	
	b = math.sqrt(2+b)
	
	c *= (2/b)

pi = round(c,3)

print('Approximation of pi:',pi)
print('Enter the radius:')
radius = input()

radint = eval(radius)

area = (c)*(radint*radint)

area1 = round(area,3)

print('Area:',area1)
