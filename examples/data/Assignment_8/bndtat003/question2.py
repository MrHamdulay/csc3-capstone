#Program that checks for repeating letters
#Matthew Bandama
#BNDTAT003
#07-April-14'''

def count_repeats(string):
	if len(string) % 2 == 0:
		if len(string) == 0:
			return(0)
		
		elif string[0] != string[1]:
			string = string[1:]
			return(count_repeats(string))
		
		elif string[0] == ' ':
			string = string[1:]
			return(count_repeats(string))
		
		else:
			string = string[2:]
			return(1+count_repeats(string))
			
	else:
		if len(string) == 1:
			return(0)
		
		elif string[0] != string[1]:
			string = string[1:]
			return(count_repeats(string))
		
		elif string[0] == ' ':
			string = string[1:]
			return(count_repeats(string))
		
		else:
			string = string[2:]
			return(1+count_repeats(string))





def main():
	
	print('Enter a message:')
	string = input()
	num = count_repeats(string)
	print('Number of pairs: ',end='')
	print(num)

if __name__=='__main__':
	main()
