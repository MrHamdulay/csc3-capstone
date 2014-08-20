""" Program to encrypt a message shifting each letter up by one
Axel du Plessis
09/05/2014"""
def encrypt(message, encrypted):
    if len(message) == 0:         
        return encrypted
    else:
        if message[0] == 'z':
            encrypted += 'a'
            return encrypt(message[1:],encrypted) 
        elif message[0] == ' ':
            encrypted += ' '
            return encrypt(message[1:],encrypted) 
        elif message[0].isupper():
            encrypted += message[0]
            return encrypt(message[1:],encrypted) 
        elif message[0] == '.':
            encrypted += '.'
            return encrypt(message[1:],encrypted) 
        else:         
            shiftCharNum = ord(message[0])+1
            encrypted += chr(shiftCharNum) 
            return encrypt(message[1:],encrypted)  

message = input("Enter a message:\n")
print("Encrypted message:\n"+encrypt(message,""))