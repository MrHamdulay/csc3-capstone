'''Encryption by recursion
Irfan Habib
2014/05/08'''

def encrypt(s):
    if s == '':
        return s
    else:
        if s[0] == 'z':
            message = 'a'
        elif s[0] == ' ':
            message = ' '
        elif s[0] == '.':
            message = '.'
        elif s[0] == s[0].upper():
            message = s[0]
        else:
            message = chr(ord(s[0])+1)
        s = s[1::]
        return message + encrypt(s)
z = encrypt(input('Enter a message:\n'))
print('Encrypted message:\n' +str(z))