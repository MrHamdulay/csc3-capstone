#Sandisha Budhal
#BDHSAN003
# 09 May 2014

# a function to encrypt message
def encrypt(msg):
    if msg == '':
        return ''
    else:
        letter_order = msg[:1]
        if (ord (letter_order)) == 122:
            return chr(97) + encrypt(msg[1:])
        elif letter_order == ' ':
            return ' ' + encrypt(msg[1:])
        elif letter_order == '.':
            return '.' + encrypt(msg[1:])
        elif 97 <= (ord(letter_order)) <= 121:
            return chr(ord(letter_order)+1) + encrypt(msg[1:])
        else:
            return letter_order + encrypt(msg[1:])        
        
#function that asks the user for an input
def encrypt_msg():
    msg = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(msg))
    
encrypt_msg()