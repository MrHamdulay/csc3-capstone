"""Recursion: encrypting lower case letters
danica van der zandt
9 may 2014"""

encrypted=""
def encrypt_lower(s):
    global encrypted
    if s.isupper():
            print("Encrypted message:\n"+ s)    
    
    else:
        if s=="":
            print("Encrypted message:\n"+encrypted)
    
        else:
                        
            if s[0]==" ":
                encrypted+=" "
                return encrypted and encrypt_lower(s[1:])
                
            elif s[0]=="z":
                encrypted+="a"
                return encrypted and encrypt_lower(s[1:])
            elif  s[0] ==".":
                encrypted+="."
                return encrypted and encrypt_lower(s[1:])
                
                
            else:
                encryption=(ord(s[0])+1)
                encrypted+=chr(encryption)                
                return encrypted and encrypt_lower(s[1:])
    
#check if lower case
#if lower case convert to ord + 4 and back to char


s=input("Enter a message:\n")
encrypt_lower(s)
