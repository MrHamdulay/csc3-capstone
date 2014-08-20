### Tashiv Sewpersad (SWPTAS001)
### CSC1015F - Assignment 8 Q3
### 08-05-2014

## Declarations
def Encode(Message):
	'''A recursive function that encodes characters'''
	# Base Case
	if Message == "":
		return ""
	# Recursive Step
	else:
		Unicode = ord(Message[0]) # find unicode - purpose : encoding
		if Unicode == 122: # Unicode 122 is "z"
			Unicode = 97 # unicode 97 is "a"
		elif 96 < Unicode < 122: # checks that it is a lowercase alphabetical character
			Unicode += 1 # used to deals with encryption shift
		return chr(Unicode) + Encode(Message[1:len(Message)])

## Live Code
sInput = input("Enter a message:\n")
print("Encrypted message:")
print(Encode(sInput))
