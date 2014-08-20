'''Program to print only the first appearance of a unique list of strings
Matthew Bandama
BNDTAT003
28-April-2014'''

def get_list():
	
	names = input()
	
	List = []
	
	while names!= 'DONE':
		
		if names not in List:
			List.append(names)
		names = input()
	
	return(List)


def main():
	
	print('Enter strings (end with DONE):')
	
	names = get_list()
	
	print()
	
	print('Unique list:')
	
	for i in names:
		print(i)

if __name__=='__main__':
	main()
