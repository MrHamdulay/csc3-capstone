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
	
	print('1 |','X'*len(mark1),sep='')
	print('2+|','X'*len(mark2),sep='')
	print('2-|','X'*len(mark2_1),sep='')
	print('3 |','X'*len(mark_3),sep='')
	print('F |','X'*len(mark_f),sep='')

def main():
	
	print('Enter a space-separated list of marks:')
	
	all_marks = question2.get_vector()
	
	mark_s = organize(all_marks)
	
	histogram(mark_s[0],mark_s[1],mark_s[2],mark_s[3],mark_s[4])


if __name__=='__main__':
	main()
