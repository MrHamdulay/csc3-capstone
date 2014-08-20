"""program to encrypt a given message
yasha longstaff
6 may 2014"""

def encrypt(s):
    first = ord(s[0])
    if s=="":
        return ''
    if len(s) >1: 
        if s[0].islower() and s[0].isalpha(): #chenk lower case and alphabetical characters
            if first == 122: #if z return a
                return 'a' + encrypt(s[1:])
            else: # move letter one up then repeat function
                return chr(ord(s[0])+1) + encrypt(s[1:])
        else: #if not lower or alpha
            return s[0] + encrypt(s[1:]) #leave character as it was then repeat function
    else:
        if first == 122: #check if last letter is z
            return 'a'
        else:
            if s[0].islower() and s[0].isalpha():
                return chr(ord(s[0])+1)
            else:
                return chr(ord(s[0]))
             
            
        
s = input('Enter a message:\n')
if s != '':
    print('Encrypted message:')
print(encrypt(s))