'''This  program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character.
Sandile Christopher Mahlangu
4 May 2014'''

def encrypt(string):
    '''This function is a recursive function that encrypts all lowercase characters to the next character'''
    if len(string)<1:
        return string
    
    elif string[0].isalpha() and string[0]==string[0].lower() and chr(ord(string[0])+1).isalpha() : #encrypt alphabets only excluding z
        #move the letter to the next one
        return chr(ord(string[0])+1) + encrypt(string[1:])
   
    elif string[0].isalpha() and string[0]==string[0].lower():
        return chr(ord(string[0])-25) + encrypt(string[1:])
    else: #if there's any other character jump to the next letter
        return string[0] + encrypt(string[1:])

if __name__=='__main__':
    string=input('Enter a message:\n')
    print('Encrypted message:\n'+encrypt(string))