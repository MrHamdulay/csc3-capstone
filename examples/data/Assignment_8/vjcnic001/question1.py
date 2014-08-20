'''Determine whether a string is a palindrome
Nicol Vojacek '''

def pal(x):
	if len(x) == 0 or len(x) == 1: #Basecase. How the program ends
		return True
	if x[0] != x[-1]: #If it is not a palindrome, we return false and stop the function
		return False
	return pal(x[1:-1]) #Keeps checking palindrome case 

x = input("Enter a string:\n")
if pal(x) == True: #If we have a palindromic string, we want it to print True
	print("Palindrome!")
else:
	print("Not a palindrome!")


