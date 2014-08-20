'''program to encrypt a message using a recursive function
nasreen hoosain
06/05/14'''

#recursive function to encrypt a string
def encrypt (string):
    if string == '':
        return string
    elif string[0] == ' ': #if there is a space, keep it
        return ' ' + encrypt(string[1:])
    elif (ord(string[0])) > 96 and ord(string[0]) < 123: #all lowercase characters
        if string[0] == 'z': #if z return a
            return 'a' + encrypt(string[1:])
        else:
            return chr(ord(string[0]) +1) + encrypt(string[1:]) #else return next lowercase letter
    else:
        return string[0] + encrypt(string[1:]) #if not lowercase, do nothing

if __name__ == '__main__':
    msg = input('Enter a message:\n')
    print('Encrypted message:')
    print(encrypt(msg))