# Emmalene Naicker
# Assignment 8

def encrypt(word):
    if len(word)<1:
        return word
    
    elif word[0].isalpha() and word[0] == word[0].lower() and chr(ord(word[0])+1).isalpha() : #encrypt alphabets but exclude z
        return chr(ord(word[0])+1) + encrypt(word[1:])
   
    elif word[0].isalpha() and word[0] == word[0].lower():
        return chr(ord(word[0])-25) + encrypt(word[1:])
    else: # jump to the next letter if another character 
        return word[0] + encrypt(word[1:])

if __name__=='__main__':
    word = input('Enter a message:\n')
    print('Encrypted message:\n'+encrypt(word))