def encrypt(x):
    if x == '':
        return '' #chr(ord(x)+1)
    elif x[0]=='z':
        return 'a' + encrypt(x[1:])
    elif not x[0].isalpha():
        return x[0] + encrypt(x[1:])
    elif x[0].isupper():
        return x[0] + encrypt(x[1:])
    else:
        return chr(ord(x[0])+1) + encrypt(x[1:])
x = input('Enter a message:\n')
print('Encrypted message:\n',encrypt(x),sep='')