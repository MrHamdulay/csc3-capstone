#Program to check if a string is a palindrome using recursion
#Matthew Bandama
#BNDTAT003
#04-May-2014

def palindrome(string):
	if len(string)%2 == 0:
		if len(string) == 0:
			return(True)

		else:
		
			if string[0] == string[-1]:
				return(palindrome(string[1:-1]))
		
			else: return(False)
	else:
		if len(string) == 0:
			return(True)

		else:
		
			if string[0] == string[-1]:
				return(palindrome(string[1:-1]))
		
			else: return(False)

def main():
	
	print('Enter a string:')
	string = input()
	
	pal = palindrome(string)
	
	if pal == True:
		print('Palindrome!')
	
	elif pal == False:
		print('Not a palindrome!')

if __name__=='__main__':
	main()
