# Najeeb Sirkhoth
# SRKMOH002
# question3.py
# Assignment 8  

# Recursive function for encrypting message
def encrypt(string): 
    if string == "":                                                    # Base Case
        return string 
    else:
        if 97 <= ord(string[0]) <= 122:                               # Check if literal lower-case
            if string[0] != "z":                                      # Check for if-not z
                return chr(ord(string[0]) + 1) + encrypt(string[1:])
            else:
                return "a" + encrypt(string[1:])
        else:
            return string[0] + encrypt(string[1:])
        

# Get input from user        
x = input("Enter a message:\n")
print ("Encrypted message:\n" + encrypt(x))     # Print encrypted message
        