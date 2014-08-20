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
