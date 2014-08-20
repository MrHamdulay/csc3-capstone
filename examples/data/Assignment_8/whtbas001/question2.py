#CSC1015F
#ASSIGNMENT 8
#QUESTION 2
#06/05/2014
#WHTBAS001  
#THOMAS WHITEHEAD

def pairs(x):
	if x == "":
		return 0
	elif len(x) != 1:
		if x[0] == x[1]:
			return 1 + pairs(x[2:]) #skips one letter forward after pair recognised and return 1
		else:
			return 0 + pairs(x[1:]) #skips one digit further
	else:
		return 0 + pairs(x[1:]) #next please!
			
string = input("Enter a message:\n")
pairs(string)
print("Number of pairs:", pairs(string))