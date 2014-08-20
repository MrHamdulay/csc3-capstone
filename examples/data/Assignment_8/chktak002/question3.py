m =input("Enter a message:\n")

def encrypt(m):
    if m=="":
        return ""
    
    elif m[0]==" " :
            return " " + encrypt(m[1:])
    
    elif (ord(m[0])==122):
        return chr(ord(m[0])-25)  + encrypt(m[1:])
    
    elif (ord(m[0])<97):
        return m[0] + encrypt(m[1:])
    
    elif (65<ord(m[0])>122):
        return encrypt(m[1:])

    else:
        return chr(ord(m[0])+1) + encrypt(m[1:])
        
        
print("Encrypted message:")
print(encrypt(m))

    
        
        
            
            