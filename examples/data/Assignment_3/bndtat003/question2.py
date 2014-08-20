# Program to make a star triangle

# Name: Matthew Bandama

# Student Number: BNDTAT003

# Date: 20-Mar-2014

height=input('Enter the height of the triangle:\n')

height1 = eval(height)

b = 1

c = height1

for a in range(height1):
	
	
	print((' '*(c-1)),('*'*b),sep='')
	b+=2
	c-=1

