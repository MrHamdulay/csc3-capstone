# Program to find palindromic primes

# Name: Matthew Bandama

# Student Number: BNDTAT003

# Date: 20-Mar-2014

def reverse1(number1):
	word = str(number1)
	word1 = word[::-1]
	word2 = int(word1)
	return(word2)

def isitprime(number):
	
	for run in range(2,(number//2+1)):
		
		if number%run==0:
			break
	else:
		return(True)



def find1():
	
	start=input('Enter the starting point N:\n')
	
	finish=input('Enter the ending point M:\n')
	
	start1 = eval(start)+1
	
	finish1=eval(finish)
	print('The palindromic primes are:')
	
	for run in range(start1,(finish1)):
		
		if run==reverse1(run) and isitprime(run)==True:
			
				print(run)


find1()
