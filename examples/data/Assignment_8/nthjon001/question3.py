"""recursively encrypts a message 
jonathan nathan 
7 may 2014"""

def encrypt(message):
    """encrypts message"""
    # base case: if message is empty, returns empty string
    if message == '':
        return ''
    # if the next character is not lower case, returns original character
    elif message[0].islower() == False:
        return message[0] + encrypt(message[1:])
    # if message contains 'z', returns the 'wrapped' 'a' 
    elif message[0] == 'z':
        return 'a' + encrypt(message[1:]) 
    # if message contains any other character, returns 'one chracter more'
    else:
        return ((chr((ord(message[0])) +1 )) + encrypt(message[1:]))

# gets input from user
message = input('Enter a message:\n')
# prints result from encrypt function	
print('Encrypted message:\n', encrypt(message), sep = '') 