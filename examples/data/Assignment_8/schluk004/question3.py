def encrypt(s):
    if len(s)==0:
        print("Encrypted message:")
        return(s)
        
    elif s[0].islower() and s[0].isalpha():
        if s[0]!="z":
            return(chr(ord(s[0])+1)+encrypt(s[1:]))
        else:
            return("a"+encrypt(s[1:]))
    else:
        return(s[0]+encrypt(s[1:]))
    
msg=input("Enter a message:\n")
print(encrypt(msg))
