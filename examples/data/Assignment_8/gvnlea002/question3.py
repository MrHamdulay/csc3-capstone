""""program usng recursion to encrypt a message
leandra govender
5 May 2014"""

# create function to encrypt message
def encrypt(message):
    if message == '':
        return ''
    else:
        letter_order = message[:1]                                #use elif statements to encrypt the message
        if (ord (letter_order)) == 122:                           #if character is z return a
            return chr(97) + encrypt(message[1:])
        elif letter_order == ' ':
            return ' ' + encrypt(message[1:])                       #if character is empty space return empty space
        elif letter_order == '.':
            return '.' + encrypt(message[1:])
        elif 97 <= (ord(letter_order)) <= 121:                    #if character is a letter return the next letter
            return chr(ord(letter_order)+1) + encrypt(message[1:])
        else:
            return letter_order + encrypt(message[1:])        
        
# funtion to input message from user and to print the new encrypted message
def encrypt_message():
    message = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(message))              #prints the encrypted message from the encrypt_message() function
    
encrypt_message()