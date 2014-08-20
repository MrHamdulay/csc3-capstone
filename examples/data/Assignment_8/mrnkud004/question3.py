"""enryption
kennedy muranda
9/5/2014"""

#define the function
def encrypt(m,f):#m=message and f=final output
    
    if m=="":
        return print(f)
    
    else:
        position = ord(m[0])#locate position of each character
        
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
        
    print(f)#encrypted message
    
m = input("Enter a message:\n")

print("Encrypted message:\n")

encrypt(m,"")
