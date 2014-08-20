#Message encrypter using recursion
#By: Luveshen Pillay
#5/5/14

# User input
msg=input("Enter a message:\n")

def encrypt(msg):
    
#key    
    if msg == "": 
         return msg
# Processing message   
    else:
        chrnum= ord(msg[0])
        
        if chrnum == 122:
            return chr(97) + encrypt(msg[1:])
            
        
        if  chrnum >= 97 and chrnum <= 121:
     
            return chr(chrnum+1) + encrypt(msg[1:])
        
        elif chrnum <= 97 or chrnum >= 122:
        
            return msg[0] + encrypt(msg[1:])    
    
print("Encrypted message:\n"+encrypt(msg))
    
    
    
    
        
        
    
    