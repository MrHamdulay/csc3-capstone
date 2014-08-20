def explode(word):
    if len(word)<1:
        return word 
    else:
        return chr((ord(word[0])+1))+explode(word[1:])
    
info=input('Enter a message:\n')

print('Encrypted message:')
x=explode(info).lower()
x=x.replace('!',' ')
print(x)



    