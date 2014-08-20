""" Assignment 8 
Question 4- encrypting
THNSIK001"""

def encrypt(message):
    """Encrypts a message"""
    if message == "":
        return ""
    elif (ord (message[0]) >=97 and ord (message[0])<122):
        return chr (ord (message[0])+1) + encrypt(message[1:])
    elif (ord (message[0])==122):
        return "a" + encrypt(message[1:])
    else:
        return message[0]+encrypt(message[1:])
    
print("Enter a message:")                       
message = input()
print("Encrypted message:\n",encrypt(message),sep="")