
'''Receive a message and return an encrypted message'''
#Enter a message:
#hello
#Encrypted message:
#ifmmp 


def code(word):
    # base case, if the lenght of the word is 1 return an empty string
    if len(word)==0:
        return ''
    # if the character's a space, return a space and search through the rest of the string
    elif word[0]==' ':
        return ' '+code(word[1:])
    # if the character's a fullstop, return a fullstop and search through the rest of the string
    elif word[0]=='.':
        return '.'+code(word[1:])
    elif word[0]=='z':
        # if the character's z, return 'a' and search through the rest of the string
            return 'a'+code(word[1:]) 
        # if the string's in uppercase, return the string/word
    elif word.isupper():
            return word       
    # otherwise change the letter to the next letter in the alphabet eg: a==b and then do the same to the other characters    
    else:
        return chr(ord(word[0]) + 1) + code(word[1:])
    

message=input('Enter a message:\n')
print('Encrypted message:')
new_message=message.split(' ')
print(code(message))

