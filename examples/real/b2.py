'''Program to get strings and right align them to the longest string
Name: Matthew Bandama
Student Number: BNDTAT003
Date: 22-April-2014'''


def get_list():
	''' Function that creates a list of the stings puts them in a list
	and stores the length of the longest word


	and returns both list and length'''

	string = ''
	my_list = []
	length = 0


	while string != 'DONE':

		string = input()

		if string != 'DONE':
			my_list.append(string)

			if length < len(string):

				length = len(string)

	return([my_list,length])


def print_out_list(list_1,num):

	for i in list_1:

		print(' '*(num-len(i))+i)

def main():

	print('Enter strings (end with DONE):')

	info = get_list()

	print()

	print('Right-aligned list:')

	print_out_list(info[0],info[1])

if __name__=='__main__':

	main()


# [bndtat003]
# [question3.py]

'''program to count the number of votes in an election
Name: Matthew Bandama
Student Number: BNDTAT003
Date: 23-April-2014'''

import question1

def count_votes(my_list):

	votes = {}

	count = 1
	for i in my_list:

		if i not in votes:

			votes[i] = count

		else:
			votes[i] = votes[i] + 1

	return(votes)

def get_candidates(names):

	candidates = []

	for i in names:

		if i not in candidates:

			candidates.append(i)

	candidates.sort()

	return(candidates)


def print_results(names,votes):
	length = 11


	for i in names:

		space = length - len(i)

		print(i,' '*space,'- ',votes[i])




def main():

	print('Independent Electoral Commission')


	print('--------------------------------')
	print('Enter the names of parties (terminated by DONE):')

	all_names = question1.get_list()

	candidates = get_candidates(all_names[0])

	votes = count_votes(all_names[0])

	print()

	print('Vote counts:')
	print_results(candidates,votes)




if __name__=='__main__':

	main()






# [bndtat003]
# [question4.py]

'''program to draw a histogram for a give range of marks


Name: Matthew Bandama
Student Number: BNDTAT003
Date: 23-April-2014'''

import question2

def organize(my_list):

	list_1 = []

	list_2_plus = []

	list_2_minus = []

	list_3 = []

	list_f = []

	for i in my_list:

		if i<50:

			list_f.append(i)

		elif 50<= i < 60:

			list_3.append(i)

		elif 60<= i <70:

			list_2_minus.append(i)

		elif 70<= i < 75:

			list_2_plus.append(i)

		elif i >= 75:

			list_1.append(i)

	return([list_1,list_2_plus,list_2_minus,list_3,list_f])


def histogram(list1,list2,list2_1,list_3,list_f):

	print('1 |','X'*len(list1))
	print('2+|','X'*len(list2))
	print('2-|','X'*len(list2_1))
	print('3 |','X'*len(list_3))
	print('F |','X'*len(list_f))

def main():

	print('Enter a space-separated list of marks:')

	all_marks = question2.get_vector()

	marks = organize(all_marks)

	histogram(marks[0],marks[1],marks[2],marks[3],marks[4])


if __name__=='__main__':
	main()


# [bndtat003]
# [question2.py]

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
