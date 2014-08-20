'''Program to simulate matrices in mathematix
Name: Matthew Bandama
Student Number: BNDTAT003
Date: 23-April-2014'''

import math

def get_vector():
	
	num = input()
	
	vector = num.split(' ')
	
	for i in range(len(vector)):
		
		vector[i] = eval(vector[i])
	
	return(vector)

def add_vector(vector_1,vector_2):
	
	new_vector = []
	
	for i in range(len(vector_1)):
		
		summation = vector_1[i] + vector_2[i]
		
		new_vector.append(summation)
	
	return(new_vector)

def multiply_vector(vector_1,vector_2):
	
	new_vector = []
	
	for i in range(len(vector_1)):
		
		multiplication = vector_1[i] * vector_2[i]
		
		new_vector.append(multiplication)
	
	answer = 0
	
	for j in (new_vector):
		
		answer = answer + j
	
	return(answer)


def norm_vector(vector):
	
	for i in range(len(vector)):
		
		vector[i] = vector[i]**2
	
	answer_sqrd = 0
	
	for j in vector:
		
		answer_sqrd += j
	
	answer = math.sqrt(answer_sqrd)
	
	rndd_answer = round(answer,2)
	
	return(rndd_answer)


def main():
	
	print('Enter vector A:')
	
	a = get_vector()
	
	print('Enter vector B:')
	
	b = get_vector()
	
	sum1 = add_vector(a,b)
	
	print('A+B =',sum1)
	
	product = multiply_vector(a,b)
	
	print('A.B =',product)
	
	norm_a = norm_vector(a)
	
	if norm_a == 0:
		print('|A| = 0.00')
	else:
		print('|A| =',norm_a)
	
	norm_b = norm_vector(b)
	
	if norm_b == 0:
		print('|B| = 0.00')
	else:
		print('|B| =',norm_b)

if __name__=='__main__':
	main()
