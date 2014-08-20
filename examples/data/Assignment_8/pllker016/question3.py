#encryption by converting lower case letters to the next letter
#kereshnee pillay
#8 may 2014

def encrypt(string):
   
    if len(string)<1:
        return string
#checking to encrypt alphabets only, coverts to lower case, excluding z    
    elif string[0].isalpha() and string[0]==string[0].lower() and chr(ord(string[0])+1).isalpha() : 
#move the letter to the next one
        return chr(ord(string[0])+1) + encrypt(string[1:])
   
    elif string[0].isalpha() and string[0]==string[0].lower():
        return chr(ord(string[0])-25) + encrypt(string[1:])
    else: 
#if character is not string, jump to next chrac ter        
        return string[0] + encrypt(string[1:])

if __name__=='__main__':
    string=input('Enter a message:\n')
    print('Encrypted message:\n'+encrypt(string))