""" Sentence encryption program
 Author: Julius Stopf0rth (STPJUL004)
 Date: 2014-05-05"""

#Get user input and lower() it's standards
msg = input("Enter a message:\n")

def encrypt(astring):
    
    # If the string is longer than a single character
    if len(astring)>1:
        # Recursive step:
        # Encrypt the first character and pass on the rest of the string.
        return encrypt(astring[0]) + encrypt(astring[1:])
    
    # If the characrter is not a space
    if astring[0] != ' ':
        
        # Check if the character is 'z'
        if astring[0] == 'z':
            # Return 'a' instead
            return 'a'
        # Otherwise, return the next letter in the alphabet
        elif (ord(astring[0])) in range(ord('a'),ord('z')):
            return chr(ord(astring[0])+1)
        else:
            return astring[0]
    
    # If the character is indeed a space, return it safely home    
    else:
        return ' '

# Procure the encrypted message and present it proudly to the user
print("Encrypted message:",encrypt(msg),end='',sep='\n')