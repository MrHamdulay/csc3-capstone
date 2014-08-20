#Kimberley Naidoo
#9 May 2014
#Message Encryption

def encrypt(string):
        if len(string)<1: #string not long enough to be encrypted
                return string
    
        elif string[0].isalpha() and string[0]==string[0].lower() and chr(ord(string[0])+1).isalpha() : #encrypt alphabets excluding z
                return chr(ord(string[0])+1) + encrypt(string[1:])
        
        elif string[0].isalpha() and string[0]==string[0].lower():      #is alphabet is z, convert to a
                return chr(ord(string[0])-25) + encrypt(string[1:])
        else:  #if there's any other character jump to the next letter
                return string[0] + encrypt(string[1:])
        
string=input('Enter a message:\n')
print('Encrypted message:\n'+encrypt(string))