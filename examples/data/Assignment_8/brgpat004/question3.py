'''Q3 of Assignment 8: Encrypting message
Patrick Boroughs
4 May 2014'''

def encrypt(string):
    
    #base case if whole string has been encrypted
    if len(string)<=0:
        return string
    
    #if next character is lower case and not z
    elif string[0].islower() and string[0]!='z':
        return chr(ord(string[0])+1)+encrypt(string[1:])
    
    #if next character is lower case z
    elif string[0]=='z':
        return 'a'+encrypt(string[1:])
    
    #if next character should not be encrypted (Upper case or non-alpha)
    else:
        return string[0]+encrypt(string[1:])

#input and printing 
print("Encrypted message:\n",encrypt(input("Enter a message:\n")),sep='')