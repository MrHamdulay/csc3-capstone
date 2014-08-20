'''Encryption
09/05/2014
Limpho Parkies'''

string=input('Enter a message:\n')
print('Encrypted message:')
def encrypt(string):
    if string.islower():
        if len(string)!=0:
            if string[0]=='z':
                print(chr(ord(string[0])-25), end='')
            elif string[0]==' ':
                print(' ', end='')
            elif string[0]=='.':
                print('.', end='')
            else:
                print(chr(ord(string[0])+1), end='')
            encrypt(string[1:])
    else:
        print(string)
        
                              
encrypt(string)