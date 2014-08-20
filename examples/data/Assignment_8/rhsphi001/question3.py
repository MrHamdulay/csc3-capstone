'''Phillip Ruhesi
05/05/2014
program to encrypt the input by moving each letter one down'''

def encrypt(x):
    if len(x)<1:
        return ''  
    elif x[0].isalpha()==False:       #if not a letter do not encrypt
        return x[0]+ encrypt(x[1:])    
    elif x[0]!=x[0].lower():          #if not lower case do not encypt
        return x[0]+ encrypt(x[1:])    
    elif x[0]=='z':                   #if letter is z encrypt to a
        return 'a'+ encrypt(x[1:])
    else:
        y=ord(x[0])+1
        return chr(y) + encrypt(x[1:]) #move every letter one place down

x=input('Enter a message:\n')
print('Encrypted message:')
print(encrypt(x))