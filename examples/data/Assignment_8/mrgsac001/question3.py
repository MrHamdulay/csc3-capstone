"""Caesar Encryption
Sachin Murugan
9/5/2014"""
code=input("Enter a message:\n")
def CaesarEncrypt(code,n):
    #set a base case
    if len(code)==0:
        return print("Encrypted message:\n"+n) 
    
    else:
        #code for shifting alphabet
        if 97<=ord(code[0])<122:
            
            p=ord(code[0])
            n=n+chr(p+1)
            CaesarEncrypt(code[1:],n)
       
        else:
            n+=code[0]
            
            CaesarEncrypt(code[1:],n)
            

CaesarEncrypt(code,"")

            
            
            
            
        
    

        
        
