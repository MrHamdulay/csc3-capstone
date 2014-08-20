"""Program to encrypt messages
Geoff Murphy
MRPGEO001
8 May 2014"""

message = input("Enter a message:\n")
encrypted = ""

def encrypt(message):
    global encrypted
    if len(message) == 0:
        return encrypted
    
    elif message[0].isalpha and ord(message[0]) < ord('a'):
        encrypted += message[0]
        return encrypt(message[1:])
    
    elif message[0].isalpha and ord(message[0]) > ord('z'):
        encrypted += message[0]
        return encrypt(message[1:])
    
    elif message[0].isalpha() and message[0] == 'z':
        encrypted += chr(97)
        return encrypt(message[1:])    
    
    elif message[0].isalpha() and ord('a') <= ord(message[0]) < ord('z'):
        encrypted += chr((ord(message[0]) + 1))
        return encrypt(message[1:])

def check(message):
    global encrypted
    encrypt(message)
    print("Encrypted message:\n", encrypted, sep = "")
    
check(message)   
