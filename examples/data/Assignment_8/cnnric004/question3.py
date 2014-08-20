message = input("Enter a message:\n")

def encrypt(encryptm,message):
    if(message != ""):
        if(ord(message[:1])<=90 and ord(message[:1])!=90):
            return encrypt(encryptm+message[:1],message[1:])
        elif(ord(message[:1])==122):
            encryptm += "a"
            return encrypt(encryptm,message[1:])
        elif(message[:1]==" "):
            encryptm += " "
            return encrypt(encryptm,message[1:])
        else:
            encryptm += chr(ord(message[:1])+1)
            return encrypt(encryptm,message[1:])
    else:
        return encryptm

print("Encrypted message:")   
print(encrypt("",message))