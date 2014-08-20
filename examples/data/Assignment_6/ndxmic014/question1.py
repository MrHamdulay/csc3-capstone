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
