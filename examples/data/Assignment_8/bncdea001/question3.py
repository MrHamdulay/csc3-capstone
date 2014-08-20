#Program to encrypt a message using recursion
#Dean Bunce
#3 May 2014

#Get input from user
msg=input("Enter a message: \n")

def encrypt(msg):
    
    #Do not change uppercase words
    if msg.isupper()==True:
        return msg
    
    
    else:
        
        #if message is empty, stop searching and return an empty string
        if msg=="":
            return ""
        
       
        #Move letters a-y, one unit up
        elif 97<=ord(msg[0])<122:
            
            new_ord=ord(msg[0])+1
            
            new_char=chr(new_ord)
            
            return new_char + encrypt(msg[1:])
        
        #If it is z, return a
        elif msg[0]=="z":
                   
               
            return "a" + encrypt(msg[1:])
        
        #Do not change spaces or fullstops
        elif msg[0]=="." or msg[0]==" ":
            
            return msg[0]+ encrypt(msg[1:])

#give output
print("Encrypted message:\n", encrypt(msg), sep="")