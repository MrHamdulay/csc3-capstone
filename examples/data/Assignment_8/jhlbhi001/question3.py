def encrypt(string,y):
    if len(string)==0:
        return print("Encrypted message:\n"+y) 
    else:
        if 97<=ord(string[0])<122: #refer to pyhton mru pg 50
            z=ord(string[0])
            y=y+chr(z+1)
            encrypt(string[1:],y)
        else:
            y+=string[0]
            encrypt(string[1:],y)
            
anything=input("Enter a message:\n")
encrypt(anything,"")

            
            
            
            
        
    

        
        
