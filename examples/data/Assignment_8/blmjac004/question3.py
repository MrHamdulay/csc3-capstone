"""encripting a message
Jacqueline Blomendahl
8 may 2014"""

msg= input("Enter a message:\n")

def encrypt(msg):
    
    if len(msg)==1:
        if msg.islower():
            
            if msg[0]=="z":
                return "a" 
            if msg[0]==" ":
                return " "
            else:
                return chr(ord(msg[0])+1) 
        else:
            return msg
    else:
        return encrypt(msg[0]) + encrypt(msg[1:])
    

    
encrypt(msg)
print("Encrypted message:")
print(encrypt(msg))