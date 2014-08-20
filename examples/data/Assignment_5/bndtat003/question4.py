# Program to draw the graph of any given function

# Name: Matthew Bandama

# Student number: BNDTAT003

# Date:16-April-2014



import math


function = input('Enter a function f(x):\n')




for run in range(10,-11,-1):
	
	
	for run2 in range(-10,11):
		
		x = run2
		y = eval(function)
		
		
		if y-0.5<= run <= y+0.5 and x-0.5<= run2 <= x+0.5:
			
			print('o',end = '')
	
		elif run == 0 and run2 == 0:
			print('+',end='')
	
		elif run == 0 and run2 != 0:
			print('-',end='')
	
		elif run2 ==0 and run != 0:
			print('|',end='')
		
					
		else:
			print(' ',end='')
	print()

