#Program for encryption

#define the function
def encrypt(m,f):
    
    if m=="":
        return print(f)
    
    else:
        position = ord(m[0])
        
        if 97<=position<122:
            position+=1
            new = chr(position)
            f = f+new
            return encrypt(m[1:],f)
        
        elif position == 122:
            excluding = "a"
            f = f+excluding
            return encrypt(m[1:],f)
        
        else:
            f+=chr(position)
            return encrypt(m[1:],f)
        
    print(f)
    
m = input("Enter a message:\n")

print("Encrypted message:")

encrypt(m,"")
