'''  to encrypt a message by converting all lowercase characters to the next characte
6 May 2014
Ednecia Matlapeng'''
encr=''
def encode(name):
    global encr
    if name=='':
        return 0
    elif name[0].islower():
        if name[0]=='z':
            encr+='a'
        else:
            temp = ord(name[0])+1
            encr+=(chr(temp))
        encode(name[1:]) 
    else:
        encr+= name[0]
        encode(name[1:])
        #return name[0]+encode(name[1:])
name = input('Enter a message:\n')
encode(name)
print('Encrypted message:\n',encr, sep='')