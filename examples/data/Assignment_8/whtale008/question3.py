"""program to change lower case to encrypt string
alexander Whiting
8 may 2014"""

def encrypt(sent):# encypts a word or sentence
    
    if sent == "":# if the string is empty returns it
        return ""
    else:
        if 122>=ord(sent[0])>=97:
                
            
            if sent[0] == "z":# z changes to a
                return 'a' + encrypt(sent[1:])
               
        
            else:
                letter = chr(ord(sent[0])+1)#gets the ordinal of the next letter and changes it to char
                return letter + encrypt(sent[1:])
        elif sent[0] == " ":
            return sent[0] + encrypt(sent[1:])            
        else:
            return sent[0] + encrypt(sent[1:])

msg = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(msg))
    
