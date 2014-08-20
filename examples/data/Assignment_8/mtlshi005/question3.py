s=input("Enter a message:\n")

def encrypt(s):
    if s=="":
        return ""
    
    elif s[0].islower():
        if s=="":
            return 0
        
                
        elif len(s)>1: 
            if s[0]=="z":
                        
                return "a" + encrypt(s[1:])            
            else:
                return chr(ord(s[0])+1)+ encrypt(s[1:])
        else:
            if s[0]=="z":
                return "a" 
            else:
                return chr(ord(s[0])+1)
    
    elif s[0].isupper():
        if len(s)>1:
            return s[0]+encrypt(s[1:])
        else:
            return s[0]
        
    else:
        if len(s)>1:
            return s[0] + encrypt(s[1:])
        else:
            return s[0]

if s!="" or s!=" ":
    print("Encrypted message:\n",encrypt(s),sep="")

