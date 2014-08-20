'''Program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character 
Daniel M. Tamale
TMLDAN001
2014-05-08'''

word=input('Enter a message:\n')
def encrypt(word):
    if word.isupper()==True:
        return word
    elif word=='':
            return '' 
    elif word[0]==' ':
        return word[0]+encrypt(word[1:])    
    elif word[0]=='z':
        return 'a'+encrypt(word[1:])
    elif word[0]=='.':
        return word+encrypt(word[1:])
    else:
        return chr(ord(word[0])+1)+encrypt(word[1:])        
print('Encrypted message:')
print(encrypt(word))
encrypt(word)