#encrypt message to transform all lower case letters with one character ahead of it
#victor gueorguiev
#03 May 2014

def encrypt(message):
    if message == '':
        return ''
    elif message[0] == 'z':
        return 'a' + encrypt(message[1:])
    elif not (message[0].isalpha() and message[0].islower()):
        return message[0] + encrypt(message[1:])
    else:
        return chr(ord(message[0])+1) + encrypt(message[1:])

def main():
    xinput = input('Enter a message:\n')
    print('Encrypted message:')
    print(encrypt(xinput))
    
main()