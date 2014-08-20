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
	
	print('1 |','X'*len(list1),sep='')
	print('2+|','X'*len(list2),sep='')
	print('2-|','X'*len(list2_1),sep='')
	print('3 |','X'*len(list_3),sep='')
	print('F |','X'*len(list_f),sep='')

def main():
	
	print('Enter a space-separated list of marks:')
	
	all_marks = question2.get_vector()
	
	marks = organize(all_marks)
	
	histogram(marks[0],marks[1],marks[2],marks[3],marks[4])


if __name__=='__main__':
	main()
