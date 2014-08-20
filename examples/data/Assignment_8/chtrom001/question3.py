# question3.py
# A program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a)
# romelon chetty
# 08 may 2014

def get_message():
    # The function that gets the input message
    
    message = input("Enter a message:\n")
    
    return message

def encrypt(message):
    # This function is used to encrypts the message
    
    if len(message) == 0:
        return ''
    else:
        if message[0].isalpha()==False:
            return message[0] + encrypt(message[1:])
            
       
        # to check if the first letter is capital
        elif message[0].isupper()==True:
            return message[0] + encrypt(message[1:])
        
        # to check if the letter is a 'z'
        elif message[0] == 'z':
            return 'a' + encrypt(message[1:])
        
        # to check if the character is a space
        elif message[0] == ' ':
            return ' ' + encrypt(message[1:])
        
        else:
            return chr( ord(message[0])+1 ) + encrypt(message[1:])
       
    
def main():
     # The mian function which is used to run the program and call the other functions
    
    message = get_message()
    encrypted = encrypt(message)
    
    print("Encrypted message:")
    print(encrypted)
    
main()
    