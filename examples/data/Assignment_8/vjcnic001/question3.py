'''Encrypting a word by changing each lower case letter by one
Nicol Vojacek'''

def encrypt(x):
	if len(x) < 1: #Basecase: If no more string, exit function
		return ""
	elif (x[:1]).isupper() == True: #If upper case letter, don't encrypt
		return x[:1] + encrypt(x[1:])
	elif x[:1] == "z":
		return "a" + encrypt(x[1:]) #If letter is "z", we want to convert it to "a"
	elif x[:1] == " ":
		return " " + encrypt(x[1:])
	elif x [:1] == ".":
		return "." + encrypt(x[1:])
	else:
		b = ord(x[:1]) + 1
		return chr(b) + encrypt(x[1:]) #Convert letter to ordinal value and add value of one, then return the character and rest of string. 
	
		
x = input("Enter a message:\n")
print("Encrypted message:\n" +encrypt(x))
