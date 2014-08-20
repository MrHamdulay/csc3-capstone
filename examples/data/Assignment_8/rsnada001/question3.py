'''Adam Rosendorff RSNADA001
03 May 2014
CSC1015F Assignment 8 Q3'''
def encrypt(text):
    if text == '':
        return text
    if text[0].isalpha() and text[0].islower():
        if text[0] == 'z':
            return 'a' + encrypt(text[1:])
        return chr(ord(text[0])+1) + encrypt(text[1:])
    else:
        return text[0] + encrypt(text[1:])
userin = input('Enter a message:\n')
print('Encrypted message:')
print(encrypt(userin))
