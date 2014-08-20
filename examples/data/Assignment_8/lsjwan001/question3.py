# Program uses recursive function to encrypt a message
# Wandile Lesejane
# 8 May 2014

def encrypt(message):
    # define an encrypt message 
    if message=="":
        return message
    else:
        if message[0]==message[0].upper():
            return message[0]+encrypt(message[1:])
        elif message[0]==" ":
            return message[0]+encrypt(message[1:])
        elif message[0]=='z':
                return 'a'+encrypt(message[1:])
        else:
            return chr(ord(message[0])+1)+encrypt(message[1:])
 
#print out theencrypt message       
message= input('Enter a message:\n')
print('Encrypted message:')
print(encrypt(message))