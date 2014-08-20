# A program that uses a recursive function to encrypt a message
# Retselisitsoe Monyake
# 09 May 2014

# a function to encrypt message
def encrypt(message):
    if message == '':
        return ''
    else:
        letter_order = message[:1]
        if (ord (letter_order)) == 122:
            return chr(97) + encrypt(message[1:])
        elif letter_order == ' ':
            return ' ' + encrypt(message[1:])
        elif letter_order == '.':
            return '.' + encrypt(message[1:])
        elif 97 <= (ord(letter_order)) <= 121:
            return chr(ord(letter_order)+1) + encrypt(message[1:])
        else:
            return letter_order + encrypt(message[1:])        
        
# funtion to input message from user
def encrypt_message():
    message = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(message))
    
encrypt_message()