#Kalind Ramnarayan
#encription
#May 2014

def encription(message):
    
    if len(message)==0:
        return 0
    
    elif message[0]=="z":
        print("a",end="")
        return encription(message[1:])
    
    elif message[0].isalpha():
        if message[0]==message[0].lower():
            print((chr(ord(message[0])+1)),end="")
            return encription(message[1:])
            
            
                  
        else:
            print(message[0],end="")
            return encription(message[1:])
    else:
        print(message[0],end="")
        return encription(message[1:])
            
message=str(input("Enter a message:\n"))
print("Encrypted message:")
encription(message)

