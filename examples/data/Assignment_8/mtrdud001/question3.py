""" Encryptiong a message with recursion statements
Dudley Mutero
9 may 2014"""

def encryptamessage(message):
    """function to encrypt a message"""
    if len (message) > 0 :
        if (ord(message[0])) == (ord('z')):
            return 'a' +encryptamessage(message[1:])
        elif (ord('a')) <= ord(message[0]) < ord('z'):
            temp = chr(ord(message[0])+1)
            return temp +encryptamessage(message[1:])
        else:
            return (message[0]) +encryptamessage(message[1:])
    else: 
        return ''
    
message = input("Enter a message:\n")
print("Encrypted message:\n"+encryptamessage(message))