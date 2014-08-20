message=input("Enter a message:\n")
def encryption(message):
                
    if message =='':
        return ''  

    elif message[0].islower():
        
        if message[0]=='z':
            encrypt='a'   
        
        elif message[0]=='.':
            return '.'
        
        else:
            
            new=ord(message[0])+1
            encrypt=chr(new)
        
        return encrypt + encryption(message[1:])

    
    else:

        return message[0] + encryption(message[1:])
    
    
print("Encrypted message:")
print(encryption(message))