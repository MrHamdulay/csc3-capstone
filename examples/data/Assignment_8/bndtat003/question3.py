#Program to encrypt a program with the next set of characters in the alphabet
#Matthew Bandama
#BNDTAT003
#07-May-2014

def encrypt(string):
	
	if len(string) == 0:
		return()
	
	else:
		
		letter = ord(string[0]) + 1
		
		next_letter = chr(letter)
		
		if string[0] == ' ':
			next_letter = ' '
		
		elif string[0].isupper() == True:
			next_letter = string[0]
			
		elif string[0] == '.':
			next_letter = '.'
		elif string[0] == 'z':
			next_letter = 'a'
			
		print(next_letter,end ='')
		string = string[1:]
		
		encrypt(string)


def main():
	
	print('Enter a message:')
	string = input()
	print('Encrypted message:')
	
	encrypt(string)
	print()


if __name__=='__main__':
	main()
