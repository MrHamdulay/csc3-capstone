"""Program to encrypt message
Keshin Vittee
5 May 2014"""

message = input("Enter a message:\n")
new_message = ""

def encrypt(message):
    global new_message
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    if message[:] == "":
        print("Encrypted message:", new_message, sep = "\n")
    
    elif message[:1] == "z":
        new_message += "a" 
        return encrypt(message[1:])
    
    elif message[:1] in alpha:
        encrypted_letter = chr((ord(message[:1]) + 1))
        new_message += encrypted_letter 
        return encrypt(message[1:])
    
    else:
        new_message += message[:1]
        return encrypt(message[1:])

encrypt(message)