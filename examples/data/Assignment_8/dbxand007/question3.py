"""Cherise Dube
06 May 2014
Program to encrypt a message"""

s=input("Enter a message:\n")

def encrypt(s):
    """Encrypts a message where every letter becomes the next character and 'z' becomes 'a'"""
    if s[0].isupper()==True:
        if len(s)>1:
            return s[0]+ encrypt(s[1:])
        elif len(s)==1: 
            return s[0]
    if s[0].islower()==True:
        if len(s)>1:
            if s[0]=='z':
                return 'a'+ encrypt(s[1:])
            elif s[0]==" ":
                return " "+encrypt(s[1:])
            else:
                return chr(ord(s[0])+1) + encrypt(s[1:])            
        elif len(s)==1:
            if s[0]=='z':
                return 'a'
            else:
                return chr(ord(s[0])+1)
        
    else:
        if len(s)>1:
            if s[0]==" ":
                return " "+encrypt(s[1:])
            elif s[0]=='z':
                return 'a'+ encrypt(s[1:])            
            else:
                return s[0]+encrypt(s[1:])
        else:
            return s[0]
print("Encrypted message:\n",encrypt(s),sep="")
    
    
    