'''Program that asks user to input strings in the parameter and right aligns them


according to the longest string
Name: MICEALA NAIDOO
Student Number: NDXMIC014
Date: 22-April-2014'''


def get_list():
	''' The get list function creates a list of strings,stores the


	length of the longest word then returns list and lenght'''

	liststring = ''
	mylist = []
	length = 0


	while liststring != 'DONE':

		liststring = input()

		if liststring != 'DONE':
			mylist.append(liststring)

			if length < len(liststring):

				length = len(liststring)

	return([mylist,length])


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

	main() #calls the function main


# [ndxmic014]
# [question3.py]

'''program to count the number of votes in an election
Name: MICEALA NAIDOO
Student Number: NDXMIC014
Date: 22-April-2014'''

import question1

def countvotes(my_list):

	votes = {}

	count = 1
	for i in my_list:

		if i not in votes:

			votes[i] = count

		else:
			votes[i] = votes[i] + 1

	return(votes)



def getcandidates(names):

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


	print('Independent Electoral Commission\n--------------------------------')
	print('Enter the names of parties (terminated by DONE):')

	all_names = question1.get_list()

	candidates = getcandidates(all_names[0])

	votes = countvotes(all_names[0])

	print()

	print('Vote counts:')
	print_results(candidates,votes)




if __name__=='__main__':

	main()






# [ndxmic014]
# [question4.py]

'''program to draw a histogram


Name: MICEALA NAIDOO
Student Number: NDXMIC014
Date: 21-April-2014'''

import question2

def organize(marks):

	mark_1 = []

	mark_2_plus = []

	mark_2_minus = []

	mark_3 = []

	mark_f = []

	for i in marks:

		if i<50:

			mark_f.append(i)

		elif 50<= i < 60:

			mark_3.append(i)

		elif 60<= i <70:

			mark_2_minus.append(i)

		elif 70<= i < 75:

			mark_2_plus.append(i)

		elif i >= 75:

			mark_1.append(i)

	return([mark_1,mark_2_plus,mark_2_minus,mark_3,mark_f])


def histogram(mark1,mark2,mark2_1,mark_3,mark_f):

	print('1 |','X'*len(mark1))
	print('2+|','X'*len(mark2))
	print('2-|','X'*len(mark2_1))
	print('3 |','X'*len(mark_3))
	print('F |','X'*len(mark_f))

def main():

	print('Enter a space-separated list of marks:')

	all_marks = question2.get_vector()

	mark_s = organize(all_marks)

	histogram(mark_s[0],mark_s[1],mark_s[2],mark_s[3],mark_s[4])


if __name__=='__main__':
	main()


# [ndxmic014]
# [question2.py]

'''Program to simulate matrices in mathematix
Name: MICEALA NAIDOO
Student Number: NDXMIC014
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



