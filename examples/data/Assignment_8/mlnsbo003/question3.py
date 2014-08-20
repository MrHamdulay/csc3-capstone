'''Encryption programme
Sbongakonke Mlangeni
07 April 2014'''
#take strings
x = input('Enter a message:\n')

def encr(x):
    #uppercase condition
    if x.isupper() == True:
        return x
    #stopping condition
    elif x == '':
        return ''
    #space condition
    elif x[0] == ' ':
        return x[0] + encr(x[1:])
    #z condition
    elif x[0] == 'z':
        return 'a' + encr(x[1:])
    #fullstop condition
    elif x[0] == '.':
        return x + encr(x[1:])
    #recursive step
    else:
        return chr(ord(x[0])+1) + encr(x[1:])
print('Encrypted message:')
print(encr(x))
    
encr(x)