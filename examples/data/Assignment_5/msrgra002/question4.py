#Grant Meeser
#MSRGRA002
#15/04/2014
import math

equation= input('Enter a function f(x):\n')
	
for y in range(-10,11):
	line=''
	block=' '
	y*=-1
	for x in range(-10,11):	
		if x==0 and y==0:block='+'		
		elif x==0: block='|'
		elif y==0: block='-'
		
		if round(eval(equation.replace('x','('+str(x)+')')))==y: block='o'
		
		line+=block
		block=' '
	print(line)

