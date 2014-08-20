'''a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character 
sankara mallane
5 may 2014
'''
# a function to encrypt the message
def encryptamessage(message):
    # check the length of the function
    if len (message) > 0 :
        # if the letter is z return a 
        if (ord(message[0])) == (ord('z')):
            # continue running through the characters
            return 'a' + encryptamessage(message[1:])
        elif (ord('a')) <= ord(message[0]) < ord('z'):
            thex = chr(ord(message[0])+1)
            return thex + encryptamessage(message[1:])
        else:
            return (message[0]) + encryptamessage(message[1:])
    else: # if there are no characters
        return ''
# user input    
message = input("Enter a message:\n")

print("Encrypted message:\n"+encryptamessage(message))