"""Program to draw the graph of any given function

Name: Aunrey Baloi

Student number: BLXAMU001

Date:16-April-2014"""



import math

# enter the function
function = input('Enter a function f(x):\n')




for func in range(10,-11,-1):
	
	
	for func2 in range(-10,11):
		
		x = func2
		y = eval(function)
		
		
		if y-0.5<= func <= y+0.5 and x-0.5<= func2 <= x+0.5:
			
			print('o',end = '')
	
		elif func == 0 and func2 == 0:
			print('+',end='')
	
		elif func == 0 and func2 != 0:
			print('-',end='')
	
		elif func2 ==0 and func != 0:
			print('|',end='')
		
					
		else:
			print(' ',end='')
	print()

