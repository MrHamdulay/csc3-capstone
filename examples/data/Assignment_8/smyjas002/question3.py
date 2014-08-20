#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 8
#question 3

def encript (testStr):
	# base case, use if string has no more characters
	if len (testStr) == 0:
		return ""
	# first recursive step, tests the current character is alphanumeric and lower case and increments it if so
	elif testStr[0].isalpha() and testStr[0].islower():
		#creates the new characer by incrementing it and checking if it is a z
		if testStr[0] == "z":
			newChar = "a"
		else:
			newChar = chr(ord(testStr[0])+1)
		return newChar + encript (testStr[1:])
	#second recursive step, if the character is not alphanumeric it is left unnchanged 
	else:
		return testStr[0] + encript (testStr[1:])
		
def main():
	a = input("Enter a message:\n")
	print("Encrypted message:\n" + encript(a))

main()

"""
 Sample I/O:

Enter a message:
hello world
Encrypted message:
ifmmp xpsme
"""
