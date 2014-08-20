"""A8Q3 - Mocryption
5/3/2012
CRNKEE002"""

def main():
    message = input('Enter a message:\n')
    print('Encrypted message:')
    print(encrypt(0, message))

def encrypt(pos, message):
    if pos < len(message)-1:
        if message[pos].isalpha() and message[pos].islower() == True:
            if message[pos] == 'z':
                return 'a' + encrypt(pos+1, message)
            else:
                return chr(ord(message[pos])+1) + encrypt(pos+1, message)
        else:
            return message[pos] + encrypt(pos+1, message)
    elif pos == len(message)-1:
        if message[pos].isalpha() and message[pos].islower() == True:
            if message[pos] == 'z':
                return 'a'
            else:
                return chr(ord(message[pos])+1)
        else:
            return message[pos]
    
            
if __name__ == '__main__':
    main()