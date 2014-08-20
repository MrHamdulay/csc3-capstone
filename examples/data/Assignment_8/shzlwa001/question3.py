# Program for message encryption
# Lwazi Shezi
# 9 May 2014

def encrypt (message) :
    """ Encryption by replacing a letter in a string with the next letter"""
    # Base case when the string length is one
    if len(message) == 1 :
        if message == 'z' :
            message_encrypt = 'a'
        elif message.isalpha() == False:
            message_encrypt = message
        else : 
            if ((ord(message)>=97)):
                message_encrypt = chr(ord(message)+1)
            else:
                message_encrypt = message
        return message_encrypt
    # Recursive step
    else:
        message_encrypt = encrypt(message[0:1]) + encrypt(message[1:])
        return message_encrypt
        
        
message = input('Enter a message:\n')
if message != '':
    print('Encrypted message:\n'+encrypt(message))