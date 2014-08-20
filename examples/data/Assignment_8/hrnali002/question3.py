"""A recursive program to encrypt a message
Alison Hoernle
HRNALI002
4 May 2014"""

def encrypt(message):
    
    if message.isupper():
        return message
    
    else:
        # Base case
        if len(message) == 1:
            
            # if it's a 'z', then return an a
            if message == 'z':
                return 'a'
            
            # else return the next letter of the alphabet
            elif message.isalpha():
                return chr(ord(message) + 1)
            
            # else if its not an alphabetic letter, return that character
            else:
                return message
        
        
        elif message[0].isalpha() and message[0] != 'z': 
            return chr(ord(message[0]) + 1) + encrypt(message[1:])
            
        elif message[0] == 'z':
            return 'a' + encrypt(message[1:])
        
        else:
            return message[0] + encrypt(message[1:])
            
message = input("Enter a message:\n")
message_new = encrypt(message)
print("Encrypted message:\n", message_new, sep = '')
    