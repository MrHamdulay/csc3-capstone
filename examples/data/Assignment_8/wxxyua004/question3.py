"""Brings lower case characters to the next character
5 May 2012
Yuan-yow Wu"""

message = input("Enter a message: \n")

def encrpyt (message):
    if message == "":
        return ""
    else:
        
        if message[0] == "z":
            return "a" + encrpyt (message[1:])
        elif message[0] == message[0].lower() and message[0].isalpha():
            return chr(ord(message[0])+1) + encrpyt (message[1:])
                
        else:
            return str(message[0]) + encrpyt (message[1:])

print("Encrypted message:\n",encrpyt(message),sep="")
