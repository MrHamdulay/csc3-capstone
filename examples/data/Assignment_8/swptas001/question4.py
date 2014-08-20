### Tashiv Sewpersad (SWPTAS001)
### CSC1015F - Assignment 8 Q4
### 08-05-2014

## Uses
import sys
sys.setrecursionlimit (30000)

## Declarations
def isPalindrome(TestString):
	'''A recursive function that checks if a string is a palindrome'''
	# Base case
	if TestString == "" or len(TestString) == 1:
		return True
	# Recursive Step:	
	elif TestString[0] == TestString[-1]: # checks corresponding characters
		return isPalindrome(TestString[1:len(TestString)-1]) 
	else:
		return False # Not a palindrome

def isPrime(TestNum,Divisor):
	'''A recursive function that checks is a number is a prime'''
	# Special case (1)
	if TestNum == 1:
		return False
	# Base Case
	elif Divisor == (TestNum//2)+1: # effeciency due to running up until the TestNum//2 (+ 1 the evens) 
		return True
	# Recursive Step
	elif TestNum % Divisor == 0:
		return False # not a prime
	else:
		return isPrime(TestNum,Divisor+1)

def CheckValues(iStart,iEnd):
	'''A recursive function that checks values in a range - the prime and palindrome characteristics'''
	# Base Case
	if iStart == iEnd:
		if isPalindrome(str(iStart)) and isPrime(iStart,2): # Note Checking Palindrome first, increase effeciency
			print(iStart) # decide to print directly, helps to lower recursion memory impact (helps a lot with the 10000-20000 case)
	# Recursive Step
	else:
		if isPalindrome(str(iStart)) and isPrime(iStart,2):
			print(iStart) # is all good
			CheckValues(iStart+1,iEnd)
		else:
			CheckValues(iStart+1,iEnd) # Not palindrome and prime			

def RecursionProtector(iStart,iEnd):
	'''This is a special function that limits recursion depth by doing batch processing'''
	# This ensures that this program can handle the 10000 to 20000 case
	# Base Case
	if iStart == iEnd: 
			CheckValues(iStart,iEnd)
	# Recursive step
	else:
		if iStart + 300 < iEnd: # Choice of 300 seems to work best, but no real significance
			CheckValues(iStart,iStart+300) # Batch process
			RecursionProtector(iStart+300,iEnd)
		else:
			iJump = iEnd - iStart
			CheckValues(iStart,iStart+iJump) # batch process

## Live Code
iStart = eval(input("Enter the starting point N:\n"))
iEnd = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
RecursionProtector(iStart,iEnd) # batch process manager



