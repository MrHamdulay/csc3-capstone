#CSC1015F
#ASSIGNMENT 8
#QUESTION 1
#06/05/2014
#WHTBAS001  
#THOMAS WHITEHEAD

def rev(x):
	if x == "":	#base case for reverse function!
		return x
	else:	#take letter to the end of the shortened string
		return rev(x[1:]) + x[0] 

def main():	#main function to get input and run reverse function.
	string = input("Enter a string:\n")
	if string == rev(string):	#assesses if it is a palendrome
		print("Palindrome!")
	else:
		print("Not a palindrome!")
		
main()	#call function to run