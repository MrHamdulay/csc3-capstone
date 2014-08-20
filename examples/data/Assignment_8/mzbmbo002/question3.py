#Mbongeni Mazibuko
#MZBMBO002
#Assignment 8

encrypt=[]
def encryption(s):
    '''recursive function to encrypt a message by converting all lowercase characters to the next character '''
    global encrypt
    '''variable defined out of function'''
    s=list(s)
    if len(s)<1:
        s=s
    else:
        if s[0].isalpha() and s[0].lower()!='z' and (''.join(s)!=''.join(s).upper()):
            encrypt.append(chr(ord(s[0])+1))
        elif s[0].isalpha() and s[0].lower()=='z':
            encrypt.append(chr(ord(s[0])-25))
        else: encrypt.append(s[0])
        return encryption(s[1:])
    encrypt=''.join(encrypt)
    '''make list to string'''
    print('Encrypted message:\n',encrypt,sep='')
    
s=input('Enter a message:\n')
encryption(s)