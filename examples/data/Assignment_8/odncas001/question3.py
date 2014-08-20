"""recursive function for producing encrypted messages based on unicode position
casey o'donnell
5 may 2014"""

def message_encrypt(s):
    if s[0].isupper() or s[0]==" " or s[0]=='.':
        if len(s)==1:
            return s[0]
        else:
            return s[0]+message_encrypt(s[1:])
    else:
        if len(s)!=1:
            if s[0]=='z':
                return chr(ord(s[0])-25)+message_encrypt(s[1:])
            else:
                return chr(ord(s[0])+1)+message_encrypt(s[1:])
        else:
            if s[0]=='z':
                return chr(ord(s[0])-25)
            else:
                return chr(ord(s[0])+1)
                   
s=input("Enter a message:\n")
print("Encrypted message:\n",message_encrypt(s),sep="")
    
    