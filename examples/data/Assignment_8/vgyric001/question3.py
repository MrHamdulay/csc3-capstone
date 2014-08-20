# Question3 
# 5 May 2014
# Richard van Gysen
# encrypter

# get message
message = input("Enter a message:\n")
# DEFINE FUNCTION
def encrypt(message):
    # if nothing, return nothing
    if message == '':
        x = ''
        return x
    # upper case remains upper case
    elif message.isupper():
        return message    
    # while there are still letters, move one space down
    elif len(message)> 0:
        x = chr(ord(message[0])+1)
        # z goes back to a
        if x == '{':
            x = 'a'
            return x + encrypt(message[1:])
        # ! goes back to space
        elif x == '!':
            x = ' '
            return x + encrypt(message[1:])
        # / goes back to full stop
        elif x == '/':
            x = '.'
            return x + encrypt(message[1:])
        # return new message
        else:
            return x + encrypt(message[1:])

# print it
print("Encrypted message:\n",encrypt(message), sep ='')