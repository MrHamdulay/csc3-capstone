#String Encryption
#Paul Roux - RXXPAU008
#08 May 2014

def encrypt_message(message,encrypted):
    """Encrypts string messages by moving each character one letter forward 
    in the alphabet with a going to z when neccesary"""
    if len(message)>=1:
        if message[0].islower():
            x = ord(message[0])
            if x==ord('z'):
                x-=25
            else:
                x+=1
            encrypted+=chr(x)
            encrypt_message(message[1:],encrypted)
        else:
            encrypted+=message[0]
            encrypt_message(message[1:],encrypted)
    else:
        print("Encrypted message:",'\n'+encrypted)
        
encrypt_message(input("Enter a message:\n"), "")