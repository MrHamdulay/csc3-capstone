"""Adam Kaliski
CSC1015F Assignment 8 Q3
2014-05-08"""
res=''
def encrypt(strng):
    global res
    if strng=='':
        print('Encrypted message:\n',res,sep='')
    elif strng[0:1].isalpha() and strng[0:1].islower():
        if (ord(strng[0:1])+1)>122:
            res+=chr(ord(strng[0:1])+1-26)
            encrypt(strng[1:])
        else:
            res+=chr(ord(strng[0:1])+1)
            encrypt(strng[1:])
    else:
        res+=strng[0:1]
        encrypt(strng[1:])        
word=input('Enter a message:\n')
encrypt(word)