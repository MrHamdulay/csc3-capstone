'''Counting pairs of letters in a string
Nicol Vojacek'''

def count(x):
	if len(x) < 2: #If the string does not have at least 2 letters left there cannot be a pair
		return False
	if x[0] == x[1]: #If the pair is the same letter, increase the count by one and return the rest of the word. 
		return 1 + count(x[2:])
	else:
		return count(x[1:]) 

x = input("Enter a message:\n")
if count(x) == False:
	print("Number of pairs:", 0)
else:
	print("Number of pairs:", count(x))