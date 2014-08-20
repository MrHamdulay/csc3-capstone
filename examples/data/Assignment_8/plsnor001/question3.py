'''Uses a recursive function to encrypt a message by converting all lowercase characters to the next character 
NOKO
06 MAY 2014'''

def  encrypt(word):
    if word == '' or word.isupper() or word=='.':
        return word
    
    elif word[0]=='z':
        return 'a'+encrypt(word[1:])
    
    elif word[0]==' ':
        return ' '+encrypt(word[1:])
        
    
    else:        
        return chr(ord(word[0])+1)+encrypt(word[1:])

word=input('Enter a message:\n')        
print('Encrypted message:\n'+encrypt(word))