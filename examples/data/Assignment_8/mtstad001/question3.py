"""Tadiwanashe Mautsa 
9th may 2014
ass8 to encrypt"""

en=''
def encode(n):
    global en
    if n=='':
        return 0
    elif n[0].islower():
        if n[0]=='z':
            en+='a'
        else:
            temp = ord(n[0])+1
            en+=(chr(temp))
        encode(n[1:]) 
    else:
        en+= n[0]
        encode(n[1:])
        #return name[0]+encode(name[1:])
n = input('Enter a message:\n')
encode(n)
print('Encrypted message:\n',en, sep='')