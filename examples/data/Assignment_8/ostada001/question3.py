''' next alphabetical character encryption 
Adam Oosthuizen ostada001'''

def encrypt(s):
    ''' returns a string with encrypted lowercase letters'''
    
    if s =='':
    #Checks if the string has been entirely process
        return ''
    if s[0] == 'z':
    #Checks for the instance of a z
        return 'a'+ encrypt(s[1:len(s)])
    elif s[0].isalpha() == True and s[0].islower():
    #Checks if the first character is alphabetic and lower case
        return chr(ord(s[0]) + 1) + encrypt(s[1:len(s)])
    else:
        return s[0] + encrypt(s[1:len(s)])
        

s= input ("Enter a message:\n")
print("Encrypted message:")
print(encrypt(s))