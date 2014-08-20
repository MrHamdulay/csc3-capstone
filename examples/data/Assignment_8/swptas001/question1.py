### Tashiv Sewpersad (SWPTAS001)
### CSC1015F - Assignment 8 Q1
### 08-05-2014

## Declarations
def isPalindrome(TestString):
	'''A recursive function that checks if a string is a palindrome'''
	# Base case
	if (TestString == "") or (len(TestString) == 1):
		return True
	# Recursive Step:	
	elif TestString[0] == TestString[-1]: # checks corresponding characters for a match
		return isPalindrome(TestString[1:len(TestString)-1]) 
	else:
		return False # Not a palindrome

## Live Code
sInput = input("Enter a string:\n")
if isPalindrome(sInput) == True: # main program interprets functions response / modular design
	print("Palindrome!")
else:
	print("Not a palindrome!")		