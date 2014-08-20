'''program to encrypt a message
matshepo mashabela
09 may 2014'''


def encrypt(message):
    if len(message)==0:
        return ''
    if message[0].islower():
        if message[0]=="z":
            return "a" + encrypt(message[1:])
        else:
            return chr(ord(message[0])+1) + encrypt(message[1:])
    else:
        return message[0] + encrypt(message[1:])
    
message=input("Enter a message:\n")
print("Encrypted message:\n",encrypt(message),sep="")
        
        
    

        
        
        