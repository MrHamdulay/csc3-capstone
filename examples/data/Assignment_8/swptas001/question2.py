### Tashiv Sewpersad (SWPTAS001)
### CSC1015F - Assignment 8 Q2
### 08-05-2014

## Declarations
def FindRepeats(TestString):
	'''A recursive function that counts matching pairs of characters'''
	# Base Case
	if TestString == "":
		return 0
	# Recursive Step	
	elif len(TestString) == 1:
		return 0
	elif TestString[0] == TestString[1]: # checks adjacent characters
		return 1 + FindRepeats(TestString[2:len(TestString)])
	else:
		return FindRepeats(TestString[1:len(TestString)]) # doesn't match

## Live Code
sInput = input("Enter a message:\n")
iPairs = FindRepeats(sInput)
print("Number of pairs:",iPairs)
